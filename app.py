from dotenv import load_dotenv
load_dotenv()

from duckduckgo_search import DDGS
from simple_agent import SimpleAgent

research_agent = SimpleAgent(
    "You are a research agent. Provide factual information."
)

summariser_agent = SimpleAgent(
    "Summarise the content clearly and concisely."
)

email_agent = SimpleAgent(
    "Write a professional email from the summary."
)

def run_agents(topic: str) -> dict:
    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=5))

    search_text = "\n".join(r["body"] for r in results)

    research = research_agent.run(
        f"Topic: {topic}\nSearch Results:\n{search_text}"
    )
    summary = summariser_agent.run(research)
    email = email_agent.run(summary)

    return {
        "research": research,
        "summary": summary,
        "email": email
    }
