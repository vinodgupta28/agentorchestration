from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class SimpleAgent:
    def __init__(self, llm, system_prompt: str):
        self.prompt = PromptTemplate(
            input_variables=["input"],
            template=f"""
            {system_prompt}

            Input:
            {{input}}
            """
        )
        self.chain = self.prompt | llm | StrOutputParser()

    def run(self, input_text: str) -> str:
        return self.chain.invoke({"input": input_text})
