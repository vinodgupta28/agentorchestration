from dotenv import load_dotenv
load_dotenv()

from duckduckgo_search import DDGS
from simple_agent import get_llm
from langchain_core.prompts import PromptTemplate

llm = get_llm()


# -------- Helper: Safe text extractor --------
def extract_text(response):
    """
    Ensures clean plain text output from LLM responses
    """
    if hasattr(response, "content"):
        return response.content
    if isinstance(response, list):
        return "\n\n".join(
            item.get("text", "") for item in response if isinstance(item, dict)
        )
    if isinstance(response, dict):
        return response.get("text", "")
    return str(response)


def orchestrator(topic: str) -> dict:

    # -------- Web Search --------
    with DDGS() as ddgs:
        results = list(ddgs.text(topic, max_results=5))

    sources = []
    search_text = ""

    if results:
        sources = [
            {
                "title": r.get("title", "Source"),
                "url": r.get("href", "")
            }
            for r in results
        ]
        search_text = "\n".join(r.get("body", "") for r in results)

    # -------- Research Agent --------
    research_prompt = PromptTemplate(
        input_variables=["topic", "search_text"],
        template="""
        Do deep research on the topic: {topic}

        Use the following web information:
        {search_text}

        Write in clear, well-structured paragraphs.
        """
    )

    research_raw = (research_prompt | llm).invoke({
        "topic": topic,
        "search_text": search_text
    })

    research = extract_text(research_raw)

    # -------- Critic Agent --------
    critic_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        Review the following research.
        Check accuracy, clarity, and completeness.
        Provide constructive improvement suggestions.
        """
    )

    critic = extract_text(
        (critic_prompt | llm).invoke({"research": research})
    )

    # -------- Fact Check --------
    fact_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        Fact-check the following content.
        Clearly mention if there are inaccuracies.
        If none, state that clearly.
        """
    )

    fact_check = extract_text(
        (fact_prompt | llm).invoke({"research": research})
    )

    # -------- Insights --------
    insight_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        Extract 5 clear and actionable insights from the research.
        Use bullet points.
        """
    )

    insights = extract_text(
        (insight_prompt | llm).invoke({"research": research})
    )

    # -------- Summary --------
    summary_prompt = PromptTemplate(
        input_variables=["research"],
        template="""
        Summarize the research in a concise and easy-to-understand manner.
        """
    )

    summary = extract_text(
        (summary_prompt | llm).invoke({"research": research})
    )

    # -------- Email --------
    email_prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
        Write a professional email based on the summary below.
        Include a subject line and proper formatting.
        """
    )

    email = extract_text(
        (email_prompt | llm).invoke({"summary": summary})
    )

    # -------- Titles --------
    title_prompt = PromptTemplate(
        input_variables=["topic"],
        template="""
        Generate 5 catchy and professional titles for the topic.
        Use bullet points.
        """
    )

    titles = extract_text(
        (title_prompt | llm).invoke({"topic": topic})
    )

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
