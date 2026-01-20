from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun

from simple_agent import SimpleAgent

# LLM (Google Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

# Search Tool
search_tool = DuckDuckGoSearchRun()

# AGENTS

research_agent = SimpleAgent(
    llm,
    system_prompt="""
    You are a research agent.
    Use the provided search results and produce factual information.
    """
)

summariser_agent = SimpleAgent(
    llm,
    system_prompt="""
    You are a summariser agent.
    Convert the content into a clear and concise summary.
    """
)

email_agent = SimpleAgent(
    llm,
    system_prompt="""
    You are an email writing agent.
    Write a professional and formal email from the summary.
    """
)

# ORCHESTRATOR
def run_agents(topic: str) -> dict:
    search_results = search_tool.run(topic)

    research_output = research_agent.run(
        f"Topic: {topic}\nSearch Results:\n{search_results}"
    )

    summary_output = summariser_agent.run(research_output)

    email_output = email_agent.run(summary_output)

    return {
        "research": research_output,
        "summary": summary_output,
        "email": email_output
    }
