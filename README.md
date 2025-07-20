#  Stateful Agentic AI Graph

This project demonstrates advanced multi-agent AI workflows using the **Groq API**, which leverages **Language Processing Units (LPUs)** for ultra-fast inference. It integrates state-of-the-art tools like **LangGraph**, **Tavily**, and the **ReAct** framework to power intelligent, modular use cases.


## [Demo](https://drive.google.com/file/d/1MGvH6rxDsuHtYvsq9A8o1ss99NYvRlLE/view?usp=sharing)




## [App](https://agenticchat.streamlit.app/)


## ✅ Use Cases

### 🤖 Report Generation Chatbot (Orchestrator + Workers)

A powerful chatbot that dynamically generates detailed reports on any topic.

- **Architecture**: Orchestrator-Worker model built with LangGraph  
- **Mechanism**: A central orchestrator LLM breaks down the user request into subtasks, sends each to a specialized worker LLM, then merges their outputs into one cohesive report.  
- **Best suited for**: Complex, multi-step tasks.

![Orchestrator Workflow](https://github.com/user-attachments/assets/6ad7e41a-85fd-44fd-9973-a6b2b0c95e00)


### 🌐 Web-Integrated Chatbot (Tavily + ReAct)

An AI assistant that answers real-time queries using current web search results.

- **Tool**: Tavily – for fast, real-time web results  
- **Framework**: ReAct (Reason + Act)  
- **How it works**: The agent reasons through the query, takes search actions, and combines findings into informative responses.

![ReAct Reasoning Flow](https://github.com/user-attachments/assets/f932cc5d-f05e-4714-a720-14ab777e5063)


### 📰 AI News Summarizer

An automated system that fetches and summarizes the top 5 global news articles based on selected frequency:

- **Frequencies**: `daily`, `weekly`, `monthly`  
- **Pipeline**:
  1. `fetch_news`: Retrieves articles using Tavily  
  2. `summary_news`: Summarizes them using Groq models  
  3. `save_results`: Stores the result in markdown files  

![AI News Summary Pipeline](https://github.com/user-attachments/assets/aa1fd89d-c6c5-44b3-83f6-a63921989722)


## 💡 Technologies Used

- **Groq API** – Ultra-fast LLM inference using LPUs  
- **LangGraph** – Agentic workflow orchestration  
- **Tavily** – Real-time web search  
- **ReAct Framework** – Reasoning-based decision making  
- **Streamlit** – UI for real-time interactions


## 📌 Highlights

- Each use case runs **independently**, offering modularity.
- The project supports **Reflection** as an alternative to ReAct for deeper reasoning.
- Easy to **extend with external tools**: APIs, databases, custom agents, and more.


## 📁 Project Structure
```plaintext

src/
├── langgraphagenticai/
│ ├── graph/ # LangGraph flow builders
│ ├── LLMs/ # Groq-based language models
│ ├── nodes/ # Functional nodes (AI News, Chatbot, etc.)
│ ├── state/ # TypedDict definitions for states
│ ├── tools/ # Tools like Tavily for search
│ ├── ui/ # Streamlit UI components
├── app.py # Streamlit entry point
├── main.py # LangGraph app logic loader
├── README.md # Project documentation
├── requirements.txt # Python dependencies

---
