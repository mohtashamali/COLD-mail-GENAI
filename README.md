# AI-Powered Cold Email Generator 

An end-to-end AI system that generates **highly personalized cold emails for job applications** using a **GENRATIVE AI ()** approach.

The system scrapes job descriptions from the web, semantically matches them with the user’s past projects and skills (uploaded via CSV), and generates a professional cold email using an LLM.

---

## 🚀 Features

- 🌐 Scrapes real job descriptions from job links
- 📄 Accepts CSV file with skills and related projects
- 🧠 Uses ChromaDB for semantic similarity search
- ✉️ Generates structured cold emails (JSON output)
- 🎯 Includes only relevant projects based on job description
- 🖥️ Simple and interactive Streamlit UI

---


## 🧠 Architecture (Project Pipeline)

┌──────────────────────────┐
│        Streamlit UI       │
│        (Frontend)         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        User Inputs        │
│  • Name                  │
│  • LinkedIn / GitHub     │
│  • Job URL               │
│  • CSV (Skills, Projects)│
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      WebBaseLoader        │
│   (Job Description       │
│      Scraping)           │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   CSV → LangChain Docs   │
│  (Skill + Project Text)  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  Embeddings Generation   │
│ (HuggingFace MiniLM)     │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        ChromaDB           │
│   (Vector Store)          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Semantic Similarity Search│
│     (Top-K Retrieval)    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Relevant Projects (Top 3)│
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   LLM (ChatGroq + Prompt)│
│  • Context Injection     │
│  • JSON-Constrained Gen  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│     Streamlit Output      │
│ • Subject Lines           │
│ • Cold Email Body         │
└──────────────────────────┘
