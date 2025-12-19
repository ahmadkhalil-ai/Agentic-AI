#Imports needed
import os  
from dotenv import load_dotenv  
from langchain_groq import ChatGroq  
from langchain_community.utilities import SerpAPIWrapper  



load_dotenv()  


# llm AI-brain
llm = ChatGroq(
    model="llama-3.1-8b-instant",  
    temperature=0,  
    groq_api_key=os.getenv("GROQ_API_KEY")  
)


# Search tool for web-search
search = SerpAPIWrapper(
    serpapi_api_key=os.getenv("SERPAPI_API_KEY")  
)



# Main function
def ask_agent(question):
    """
    This function takes your question and either:
    1. Searches the web for an answer, OR
    2. Answers directly if it already knows
    
    Args:
        question (str): Your question as text
    
    Returns:
        str: The answer
    """
    
    # Print the question nicely
    print(f"\n{'='*60}")
    print(f"❓ YOUR QUESTION: {question}")
    print(f"{'='*60}\n")
    
  
    decision_prompt = f"""Look at this question: "{question}"

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

    # Send the decision prompt to the AI and get response
    decision_response = llm.invoke(decision_prompt)
    decision = decision_response.content.strip().upper()
    
    # Show what the agent decided
    if "YES" in decision:
        print("🔍 DECISION: I need to search the web for this\n")
    else:
        print("💭 DECISION: I can answer this directly\n")
    
  
    
    if "YES" in decision:
        print("⏳ Searching Google...\n")
        
        try:
            # Use the search tool to find information
            search_results = search.run(question)
            # search_results now contains text from top Google results
            
            print("✅ Search complete! Reading results...\n")
            
            # Now ask the AI to SUMMARIZE the search results and answer
            answer_prompt = f"""I searched Google for: "{question}"

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
            
            # Get the final answer from AI (this will be summarized)
            final_response = llm.invoke(answer_prompt)
            answer = final_response.content
            
        except Exception as e:
            # If search fails, show the error
            answer = f"❌ Search failed: {str(e)}"
    
  
    
    else:
        print("⏳ Thinking...\n")
        
        # Just ask the AI directly without searching
        direct_response = llm.invoke(question)
        answer = direct_response.content
    
  
    
    print(f"🎯 ANSWER:\n{answer}\n")
    print(f"{'='*60}\n")
    
    return answer



if __name__ == "__main__":
    # This only runs when you execute this file directly
    
    print("\n" + "="*60)
    print("🤖 RESEARCH AGENT - Ask me anything!")
    print("="*60)
    print("\nI can search the web for current info or answer directly.")
    print("Type 'quit' to exit.\n")
    
    # Loop forever until user quits
    while True:
        # Get question from user
        user_input = input("👤 You: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye! Thanks for chatting!\n")
            break
        
        # Skip empty inputs
        if not user_input:
            print("⚠️  Please ask a question!\n")
            continue
        
        # Process the question
        ask_agent(user_input)


