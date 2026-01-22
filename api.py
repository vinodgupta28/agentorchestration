from simple_agent import SimpleAgent

def run_agent(task: str, user_input: str) -> str:
    agent = SimpleAgent(system_prompt=task)
    return agent.run(user_input)
