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


## 🧠 Architecture (RAG Pipeline)


COMPLETE SYSTEM DIAGRAM
┌──────────────┐
│   Streamlit  │
│   Frontend   │
└──────┬───────┘
       │
       ▼
┌─────────────────────┐
│ User Inputs         │
│ Name, Links, CSV    │
│ Job URL             │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ WebBaseLoader       │
│ Job Description     │
└──────┬──────────────┘
       │
       ▼
┌────────────────────────────┐
│ CSV → Documents            │
│ Skill + Project            │
└──────┬─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│ Embeddings (HF MiniLM)     │
│ Vector Representation      │
└──────┬─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│ ChromaDB                   │
│ Semantic Similarity Search │
└──────┬─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│ Relevant Projects (Top 3)  │
└──────┬─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│ LLM (ChatGroq + Prompt)    │
│ JSON Email Generation      │
└──────┬─────────────────────┘
       │
       ▼
┌────────────────────────────┐
│ Streamlit Output           │
│ Subjects + Email Body      │
└────────────────────────────┘