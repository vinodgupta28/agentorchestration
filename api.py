from simple_agent import SimpleAgent

research_agent = SimpleAgent("Research Agent")

def run_agent(agent_type: str, text: str) -> str:
    if agent_type == "research":
        return research_agent.run(text)

    return "Invalid agent type"
