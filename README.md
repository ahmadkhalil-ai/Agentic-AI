#  Research Agent - AI-Powered Web Search & Summarization

An intelligent research assistant that automatically searches the web and summarizes information using AI. Built with LangChain, Groq API, and Chainlit.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

##  Features

- **Smart Web Search** - Automatically searches Google for current information
- **Intelligent Decision Making** - Decides when to search vs answer directly
- **Auto Summarization** - Condenses search results into clear, concise answers
- **Beautiful UI** - Modern chat interface with Chainlit
- **Fast & Free** - Powered by Groq's lightning-fast LLM API
- **Real-time Updates** - Shows what the agent is doing at each step

---

## 🎬 Demo

**Ask:** "Who won the last F1 race?"
- ✅ Agent searches the web
- ✅ Reads multiple sources
- ✅ Summarizes and answers

**Ask:** "What is 2 + 2?"
- ✅ Agent answers directly (no search needed)
- ✅ Fast response

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed
- **Groq API Key** (Free at [console.groq.com](https://console.groq.com))
- **SerpAPI Key** (Free tier: 100 searches/month at [serpapi.com](https://serpapi.com))

---

## 🚀 Quick Start

### 1. Clone or Download the Project

```bash
mkdir research-agent
cd research-agent
```

### 2. Install Dependencies

```bash
pip install langchain-community langchain-groq google-search-results python-dotenv chainlit
```

### 3. Create `.env` File

Create a file named `.env` in your project folder:

```env
GROQ_API_KEY=gsk_your_groq_key_here
SERPAPI_API_KEY=your_serpapi_key_here
```

**Important:** Never share or commit this file to GitHub!

### 4. Run the Agent

**Option A: Terminal Version**
```bash
python main.py
```

**Option B: Beautiful Web UI**
```bash
chainlit run app.py -w
```

Then open http://localhost:8000 in your browser!

---

## 📁 Project Structure

```
research-agent/
│
├── app.py              # Chainlit web UI version
├── main.py             # Terminal/CLI version
├── .env                # API keys (DO NOT COMMIT)
├── .gitignore          # Git ignore file
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

---

## 🎯 Usage Examples

### Example 1: Recent News
```
You: Who won the last F1 race?
Agent: 🔍 Searching the web...
Agent: Max Verstappen won the Abu Dhabi Grand Prix on December 8, 2024...
```

### Example 2: Stock Prices
```
You: What's Amazon stock price today?
Agent: 🔍 Searching the web...
Agent: Amazon (AMZN) is currently trading at $178.25...
```

### Example 3: Summarization
```
You: Summarize latest SpaceX launches
Agent: 🔍 Searching the web...
Agent: SpaceX successfully launched three Falcon 9 rockets in November 2024...
```

### Example 4: Direct Answer
```
You: What is Python?
Agent: 💭 Direct answer...
Agent: Python is a high-level programming language...
```

### Adjust Temperature

```python
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.7,  # 0 = focused, 1 = creative
)
```

### Customize Search Behavior

Edit the decision prompt in the code to change when the agent searches.

---

## 🔧 Troubleshooting

### Problem: ModuleNotFoundError

**Solution:**
```bash
pip install langchain-community langchain-groq google-search-results python-dotenv chainlit
```

### Problem: Invalid API Key

**Solution:**
1. Check your `.env` file
2. Make sure there are no spaces around the `=` sign
3. Verify keys are correct from the dashboards

### Problem: Search Fails

**Solution:**
1. Check you haven't exceeded 100 free searches on SerpAPI
2. Verify your SerpAPI key is active
3. Check your internet connection

### Problem: Chainlit Won't Start

**Solution:**
```bash
# Make sure chainlit is installed
pip install chainlit

# Run with full path
python -m chainlit run app.py -w
```

---

## 📦 Requirements

Create `requirements.txt`:

```txt
langchain-community>=0.0.13
langchain-groq>=0.0.1
google-search-results>=2.4.2
python-dotenv>=1.0.0
chainlit>=1.0.0
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🎨 Customizing the UI

### Change Theme Colors

Create `.chainlit/config.toml`:

```toml
[UI]
name = "My Research Agent"
default_collapse_content = true

[UI.theme]
primary_color = "#2563eb"
background_color = "#ffffff"
font_family = "Inter, sans-serif"
```

### Add Custom Logo

Place your logo in `.chainlit/public/logo.png`

---

## 🧪 How It Works

### Architecture

```
User Question
     ↓
Decision Engine (LLM)
     ↓
  Search?
     ↓
YES → Google Search → Summarize → Answer
NO  → Direct Answer
     ↓
Display Result
```

### Key Components

1. **LLM (Large Language Model)**
   - Brain of the agent
   - Makes decisions
   - Summarizes information
   - Powered by Groq (llama-3.1-70b)

2. **Search Tool**
   - Uses SerpAPI
   - Searches Google
   - Returns top results

3. **Agent Logic**
   - Analyzes questions
   - Decides search vs direct
   - Processes results
   - Formats answers

4. **Chainlit UI**
   - Beautiful chat interface
   - Real-time updates
   - Status indicators

---

## 💰 Cost Breakdown

### Free Tier (Perfect for Learning)

- **Groq API:** FREE unlimited usage
- **SerpAPI:** FREE 100 searches/month
- **Hosting:** FREE (runs locally)

**Total Cost:** $0/month for learning and testing!

### If You Need More Searches

- **SerpAPI Paid:** $50/month for 5,000 searches
- **Alternative:** Switch to Bing Search API (different pricing)

---

## 🚀 Deployment

### Deploy to Replit

1. Go to [replit.com](https://replit.com)
2. Create new Python Repl
3. Upload your files
4. Add secrets (API keys) in Replit's Secrets tab
5. Run `chainlit run app.py`

### Deploy to Hugging Face Spaces

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space (Chainlit template)
3. Upload your code
4. Add API keys as secrets
5. Deploy!

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see below:

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎓 Learning Resources

### Want to Learn More?

- **LangChain Docs:** [docs.langchain.com](https://docs.langchain.com)
- **Groq Documentation:** [console.groq.com/docs](https://console.groq.com/docs)
- **Chainlit Docs:** [docs.chainlit.io](https://docs.chainlit.io)
- **SerpAPI Docs:** [serpapi.com/docs](https://serpapi.com/docs)

### Video Tutorials

- Search "LangChain agents tutorial" on YouTube
- Search "Chainlit tutorial" for UI guides

---

## 🐛 Known Issues

1. **Search Rate Limit:** Free tier limited to 100 searches/month
2. **Long Responses:** Some summaries might be verbose (working on it)
3. **Decision Accuracy:** Occasionally searches when not needed

---


## ❓ FAQ

**Q: Is this really free?**  
A: Yes! Both Groq and SerpAPI free tiers are perfect for learning.

**Q: Can I use this commercially?**  
A: Yes, but you'll need paid API plans for higher usage.

**Q: Can I add more tools?**  
A: Absolutely! LangChain supports many tools (calculator, Wikipedia, etc.)

**Q: Does it store my conversations?**  
A: No, everything runs locally. Nothing is saved unless you add that feature.

**Q: Can I change the LLM provider?**  
A: Yes! You can use OpenAI, Anthropic, or any LangChain-supported LLM.

---

## 📧 Contact & Support

- **Issues:** Open an issue on GitHub
- **Questions:** Create a discussion on GitHub
- **Email:** your-email@example.com (optional)

---

## 🙏 Acknowledgments

- **LangChain** - For the amazing agent framework
- **Groq** - For free, fast LLM API
- **Chainlit** - For the beautiful UI framework
- **SerpAPI** - For reliable web search

---

## ⭐ Star This Project

If you find this helpful, please give it a star! ⭐

---


**Last Updated:** December 2025



*Happy Researching! 🚀*
