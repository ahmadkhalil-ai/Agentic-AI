

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper
import chainlit as cl  # This creates the beautiful UI



load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Create search tool
search = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))



@cl.on_chat_start
async def start():
    """
    This runs when someone opens your app
    Shows a welcome message
    """
    
    # Send welcome message with emoji and styling
    await cl.Message(
        content="""# 🤖 Welcome to Research Agent!
        
I'm your intelligent research assistant powered by AI and web search.

## What I can do:
- 🔍 **Search the web** for current information
- 📰 **Find latest news** and events
- 💰 **Get stock prices** and market data
- 🏎️ **Sports results** and scores
- 📝 **Summarize** information clearly
- 💭 **Answer** general knowledge questions

## How to use:
Just type your question and I'll either:
- Search the web if it's current information
- Answer directly if I already know

**Try asking:**
- "Who won the last F1 race?"
- "Summarize latest SpaceX news"
- "What's Amazon stock price today?"

---
Ready to help! Ask me anything! 👇
        """
    ).send()



@cl.on_message
async def main(message: cl.Message):
    """
    This runs every time user sends a message
    
    Args:
        message: The user's question
    """
    
    # Get the user's question
    user_question = message.content
    

    
    msg = cl.Message(content="")
    await msg.send()
    
    # Update message to show we're analyzing
    msg.content = "🤔 Analyzing your question..."
    await msg.update()
    

    
    decision_prompt = f"""Look at this question: "{user_question}"

Should I search the web to answer this?

Say YES if:
- It's about recent news or current events
- It's about today's prices or stock values
- It's about recent sports results
- It's about anything that happened recently

Say NO if:
- It's simple math (like 2+2)
- It's general knowledge that doesn't change
- You already know the answer

Answer ONLY: YES or NO"""

    # Get decision from AI
    decision_response = llm.invoke(decision_prompt)
    decision = decision_response.content.strip().upper()
    
   
    
    if "YES" in decision:
        # Update status
        msg.content = "🔍 Searching the web for latest information..."
        await msg.update()
        
        try:
            # Search Google
            search_results = search.run(user_question)
            
            # Update status
            msg.content = "📖 Reading and summarizing results..."
            await msg.update()
            
            # Ask AI to summarize
            answer_prompt = f"""I searched Google for: "{user_question}"

Here are the search results:
{search_results}

Your task:
1. Read all the search results carefully
2. Extract the most important information
3. Summarize it in a clear, concise way
4. Answer the original question

If the question asks for a summary (like "summarize latest SpaceX launches"):
- Keep it to 3-4 sentences maximum
- Focus on the most recent and important information
- Be specific with dates and facts

Answer:"""
            
            # Get final answer
            final_response = llm.invoke(answer_prompt)
            answer = final_response.content
            
            # Format the final response with icon
            final_message = f"🔍 **Web Search Result:**\n\n{answer}"
            
        except Exception as e:
            final_message = f"❌ Search failed: {str(e)}"
    
  
    
    else:
        # Update status
        msg.content = "💭 Thinking... (no search needed)"
        await msg.update()
        
        # Get direct answer
        direct_response = llm.invoke(user_question)
        answer = direct_response.content
        
        # Format the final response with icon
        final_message = f"💭 **Direct Answer:**\n\n{answer}"
    
  
    
    msg.content = final_message
    await msg.update()
