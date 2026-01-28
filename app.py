from dotenv import load_dotenv
load_dotenv()

from duckduckgo_search import DDGS
from simple_agent import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()

def orchestrator(topic: str) -> dict:

    # -------- Web Search --------
    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=5))

    sources = [
        {"title": r["title"], "url": r["href"]}
        for r in results
    ]

    search_text = "\n".join(r["body"] for r in results)

    # -------- Research Agent --------
    research_prompt = PromptTemplate(
        input_variables=["topic", "search_text"],
        template="""
        Do deep research on the topic: {topic}
        Use the following web data:
        {search_text}
        Write in clear paragraphs.
        """
    )
    research = (research_prompt | llm).invoke({
        "topic": topic,
        "search_text": search_text
    }).content   

    # -------- Critic Agent --------
    critic_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        Review the following research.
        Check accuracy, clarity, and completeness.
        Give improvement suggestions.
        """
    )
    critic = (critic_prompt | llm).invoke({
        "research": research
    }).content

    # -------- Fact Check --------
    fact_prompt = PromptTemplate(
        input_variables=["research"],
        template="Fact-check the following content and highlight inaccuracies:\n{research}"
    )
    fact_check = (fact_prompt | llm).invoke({
        "research": research
    }).content

    # -------- Insights --------
    insight_prompt = PromptTemplate(
        input_variables=["research"],
        template="Extract 5 key insights from the following research:\n{research}"
    )
    insights = (insight_prompt | llm).invoke({
        "research": research
    }).content

    # -------- Summary --------
    summary_prompt = PromptTemplate(
        input_variables=["research"],
        template="Summarize the following research clearly:\n{research}"
    )
    summary = (summary_prompt | llm).invoke({
        "research": research
    }).content

    # -------- Email --------
    email_prompt = PromptTemplate(
        input_variables=["summary"],
        template="Write a professional email using this summary:\n{summary}"
    )
    email = (email_prompt | llm).invoke({
        "summary": summary
    }).content

    # -------- Titles --------
    title_prompt = PromptTemplate(
        input_variables=["topic"],
        template="Generate 5 catchy titles for the topic: {topic}"
    )
    titles = (title_prompt | llm).invoke({
        "topic": topic
    }).content

    return {
        "research": research,
        "critic": critic,
        "sources": sources,
        "fact_check": fact_check,
        "insights": insights,
        "summary": summary,
        "email": email,
        "titles": titles
    }
