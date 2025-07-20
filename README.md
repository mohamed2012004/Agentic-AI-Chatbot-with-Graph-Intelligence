#### 🚀 Agentic AI Project

This project demonstrates advanced AI workflows using the **Groq API**, which leverages **LPU (Language Processing Units)** for ultra-fast inference. I utilized three Groq-hosted models and built intelligent workflows using **LangGraph**, **Tavily**, and the **ReAct** framework.

---

#### ✅ Use Cases

---

#### 🤖 Report Generation Chatbot (Orchestrator + Workers)

This chatbot generates detailed reports on any topic provided by the user.

- **Workflow**: Orchestrator-Workers using LangGraph  
- **How it works**: A central LLM dynamically decomposes the task into subtasks, distributes them to 5 specialized worker LLMs, and combines their outputs into a single report.  
- **Best for**: Complex queries where subtasks aren't predefined.

<img width="138" height="450" alt="Orchestrator Workflow" src="https://github.com/user-attachments/assets/6ad7e41a-85fd-44fd-9973-a6b2b0c95e00" />

---

#### 🌐 Chatbot Integrated with Web Search (Tavily + ReAct)

This chatbot answers real-time questions using live web data.

- **Tool**: Tavily (for real-time web search)  
- **Framework**: ReAct (Reasoning + Acting)  
- **How it works**: Uses reasoning steps and action plans to search and answer based on current information.

<img width="226" height="260" alt="ReAct Reasoning Flow" src="https://github.com/user-attachments/assets/f932cc5d-f05e-4714-a720-14ab777e5063" />

---

#### 📰 AI News Summary

Automatically summarizes the top 5 news articles globally, categorized by frequency: **daily**, **weekly**, and **monthly**.

- **Pipeline**:
  1. **fetch_news**: Retrieves top articles via Tavily  
  2. **summary_news**: Summarizes articles using Groq models  
  3. **save_results**: Stores summaries in a markdown file  

<img width="169" height="453" alt="AI News Summary Pipeline" src="https://github.com/user-attachments/assets/aa1fd89d-c6c5-44b3-83f6-a63921989722" />

---

#### 💡 Technologies Used

- **Groq API** – for ultra-fast LLM inference  
- **LangGraph** – for multi-agent workflows  
- **Tavily** – real-time web search integration  
- **ReAct Framework** – for reasoning-based decision-making  

---

#### 📌 Notes
- You can run each use case independently.  
- You can use the **Reflection** framework as an alternative to **ReAct** for enhanced reasoning and decision-making.  
- You can integrate the system with many external tools (e.g., web search, file storage, APIs, databases) to extend functionality.  

---
<pre> src/ ├── langgraphagenticai/ │ ├── graph/ # Builds and visualizes LangGraph flow logic │ ├── LLMs/ # Handles LLM interaction (Groq models, etc.) │ ├── nodes/ # Contains nodes used within LangGraph (AI News, Chatbot) │ ├── state/ # Stores TypedDict-based state definitions per use case │ ├── tools/ # Custom tools like search integrations (Tavily, etc.) │ ├── ui/ # UI components for Streamlit (displays, config) ├── app.py # Streamlit entrypoint for launching the app ├── main.py # Main script for loading LangGraph app logic ├── README.md # Project documentation and setup ├── requirements.txt # Python dependencies </pre>
