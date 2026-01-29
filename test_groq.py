from simple_agent import get_llm

llm = get_llm()
print(llm.invoke("Say hello in one line").content)
