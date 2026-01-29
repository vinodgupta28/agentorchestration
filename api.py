from simple_agent import get_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def run_multi_agent_workflow(topic: str):
    llm = get_llm()
    parser = StrOutputParser()

    # -------- Research Agent --------
    research_prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
You are a senior research analyst.

Write a detailed, well-explained article on the topic below.
Use clear paragraphs.
Avoid markdown, bullets, or headings.
Tone should be academic yet easy to understand.

Topic: {topic}
"""
    )

    research_output = (
        research_prompt | llm | parser
    ).invoke({"topic": topic})

    # -------- Critic Agent --------
    critic_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
You are a quality reviewer.

Analyze the research below.
State clearly whether it is sufficient and why.
Give improvement suggestions if any.

Research:
{research}
"""
    )

    critic_output = (
        critic_prompt | llm | parser
    ).invoke({"research": research_output})

    # -------- Summary Agent --------
    summary_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
Create a high-quality executive summary of the research below.
Write in 2–3 strong paragraphs.
Do not repeat sentences.
Keep it crisp, professional, and informative.

Research:
{research}
"""
    )

    summary_output = (
        summary_prompt | llm | parser
    ).invoke({"research": research_output})

    # -------- Email Agent --------
    email_prompt = PromptTemplate(
        input_variables=["summary", "topic"],
        template="""
Write a professional formal email based on the summary below.

Email format:
Subject:
Greeting:
Body (2 short paragraphs):
Closing:

Topic: {topic}

Summary:
{summary}
"""
    )

    email_output = (
        email_prompt | llm | parser
    ).invoke({"summary": summary_output, "topic": topic})

    return {
        "research": research_output,
        "critic": critic_output,
        "summary": summary_output,
        "email": email_output
    }
