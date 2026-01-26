from langchain_core.prompts import PromptTemplate

RESEARCH_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a research assistant.
Do deep research on the topic below.
Use bullet points and examples.

Topic:
{topic}
"""
)

CRITIC_PROMPT = PromptTemplate(
    input_variables=["research", "topic"],
    template="""
You are a Quality Assurance Analyst.

Evaluate the research below.

Research:
{research}

Topic:
{topic}

Respond ONLY in JSON:
{{
  "is_sufficient": true or false,
  "feedback": "what is missing or how to improve"
}}
"""
)

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["research"],
    template="""
Summarize the following research clearly:

{research}
"""
)

EMAIL_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template="""
Write a professional email based on the summary below:

{summary}
"""
)
