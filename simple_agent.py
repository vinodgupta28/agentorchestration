import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.4,
        api_key=api_key
    )

llm = get_llm()

# 🔴 YAHI SAHI TARIKA HAI
def llm_text(prompt: str) -> str:
    response = llm.invoke([("human", prompt)])
    return response.content


def run_multi_agent_workflow(topic):
    research = llm_text(f"Provide detailed research on: {topic}")
    critic = llm_text(f"Critically review the research on: {topic}")
    fact_check = llm_text(f"Fact check the research on: {topic}")
    insights = llm_text(f"Give 3 key insights on: {topic}").split("\n")
    summary = llm_text(f"Write a short summary on: {topic}")
    email = llm_text(f"Write a professional email on: {topic}")
    titles = llm_text(f"Give 3 titles on: {topic}").split("\n")

    sources_raw = llm_text(f"Give 3 sources with title - url for: {topic}")
    sources = []
    for line in sources_raw.split("\n"):
        if " - " in line:
            t, u = line.split(" - ", 1)
            sources.append({"title": t.strip(), "url": u.strip()})

    if not sources:
        sources = [{"title": "Example", "url": "https://example.com"}]

    return {
        "research": research,
        "critic": critic,
        "sources": sources,
        "fact_check": fact_check,
        "insights": insights,
        "summary": summary,
        "email": {"text": email},
        "titles": titles
    }
