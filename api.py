from simple_agent import SimpleAgent
from memory import Memory

def run_multi_agent(topic: str):
    memory = Memory()

    # Research Agent
    research_agent = SimpleAgent(
        "You are a research assistant. Do deep research with bullet points."
    )
    research = research_agent.run(f"Topic: {topic}")
    memory.save("research", research)

    # Summary Agent (uses memory)
    summary_agent = SimpleAgent(
        "You are a summarization assistant."
    )
    summary = summary_agent.run(memory.get("research"))
    memory.save("summary", summary)

    # Email Agent (uses memory)
    email_agent = SimpleAgent(
        "You are a professional email writer."
    )
    email = email_agent.run(memory.get("summary"))
    memory.save("email", email)

    return memory.store
