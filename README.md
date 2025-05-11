# 🧠 Real-Time Search Engine Chatbot

A real-time AI chatbot that integrates Google Search with the Groq LLaMA3-70B model to deliver up-to-date, professional, and context-aware responses. Built for smart automation, future-ready chat systems, and research support.

> 🚧 Now working on integrating **Cohere's Query Classification API** for better intent detection and routing!

---

## ✨ Features

- 🌐 **Google Search Integration**  
  Pulls top search results with descriptions using `googlesearch-python`.

- 🧠 **Groq (LLaMA3-70B) Response Generation**  
  Provides contextual, structured answers based on real-time info and user queries.

- 🗃️ **Chat History Logging**  
  Stores the full conversation in a local JSON file (`chatbot.json`).

- 🕒 **Real-Time Metadata**  
  Date, time, and day info included in the system prompt for dynamic context.

- 🔐 **Secure Environment Management**  
  API keys and config are managed via `.env` file.

---

## 📦 Project Structure

    realtimesearchenginebot/
    |── chatbot.json # Conversation log
    ├── chatbot.py # Main application script
    ├── .env # Environment variables (not tracked)
    ├── requirements.txt # Project dependencies
    └── README.md # This file


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mega123-art/realtimesearchenginebot.git
cd realtimesearchenginebot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python realtime.py