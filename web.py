import os
from dotenv import load_dotenv
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")
parser = JsonOutputParser()
llm = ChatGroq(
    api_key=GROQ_KEY,
    model="llama-3.1-8b-instant",
    temperature=0,
)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def generate_cold_email(link, name, linkedin, github, csv_file):
    scraped_data = WebBaseLoader(link).load()[0].page_content
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.lower().str.strip()

    if not {"skill", "project"}.issubset(df.columns):
        raise ValueError("CSV must contain 'skill' and 'project' columns")
    docs = []
    for _, row in df.iterrows():
        docs.append(
            Document(
                page_content=f"Skill: {row['skill']} | Project: {row['project']}"
            )
        )

    # 4️⃣ Store in Chroma (in-memory)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name="user_projects"
    )

    # 5️⃣ Retrieve top matching projects
    relevant_docs = vectordb.similarity_search(
        scraped_data,
        k=3
    )

    projects_text = "\n".join(
        doc.page_content for doc in relevant_docs
    )

    # 6️⃣ Prompt
    prompt = PromptTemplate.from_template(
        """
        Return ONLY valid JSON. No extra text.

        JSON format:
        {{
          "subject_lines": ["...", "...", "..."],
          "email_body": "..."
        }}

        Write a professional cold email for a job application.

        Candidate Details:
        - Name: {name}
        - LinkedIn: {linkedin}
        - GitHub: {github}

        Relevant Projects (use naturally, not as a list):
        {projects}

        Requirements:
        - 3 subject lines
        - 150–170 words
        - Clear CTA
        - Professional yet conversational tone

        Job Description:
        {job_description}
        """
    )

    chain = prompt | llm | parser

    result = chain.invoke({
        "name": name,
        "linkedin": linkedin,
        "github": github,
        "projects": projects_text,
        "job_description": scraped_data
    })

    return result
