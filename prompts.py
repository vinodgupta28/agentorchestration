from langchain_core.prompts import PromptTemplate

# ---------------- RESEARCH PROMPT ----------------
RESEARCH_PROMPT = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a professional research analyst.

Do deep research on the topic below and write the output
in well-structured paragraphs (NOT bullet points).

Guidelines:
- Clear explanation
- Real-world examples
- Technical + practical view
- Easy to understand language

Topic:
{topic}
"""
)

# ---------------- CRITIC PROMPT ----------------
CRITIC_PROMPT = PromptTemplate(
    input_variables=["research", "topic"],
    template="""
You are a Quality Assurance Analyst.

Analyze the research content strictly.

Research:
{research}

Topic:
{topic}

Respond ONLY in valid JSON format:
{
  "is_sufficient": true or false,
  "feedback": "clear improvement suggestions in text"
}
"""
)

# ---------------- SUMMARY PROMPT ----------------
SUMMARY_PROMPT = PromptTemplate(
    input_variables=["research"],
    template="""
Create a clear, concise summary in paragraph form
from the research below:

{research}
"""
)

# ---------------- EMAIL PROMPT ----------------
EMAIL_PROMPT = PromptTemplate(
    input_variables=["summary"],
    template="""
Write a professional and formal email
based on the summary below.

The email should:
- Have a greeting
- Clearly explain the topic
- End with a polite closing

Summary:
{summary}
"""
)
