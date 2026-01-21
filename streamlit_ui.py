import streamlit as st
from google import genai

# -------------------------
# 🔑 Gemini API Setup
# -------------------------
API_KEY = "AIzaSyCgH1b9tAENsJyP4J9FZB4NLNYfefOdgiw"  
client = genai.Client(api_key=API_KEY)

# -------------------------
# Streamlit Page Config
# -------------------------
st.set_page_config(
    page_title="Orchestration UI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------------
# Page Title
# -------------------------
st.title("Agent Orchestration")

# -------------------------
# Tabs
# -------------------------
tab1, tab2, tab3 = st.tabs(["Research Data", "Summary", "Draft Email"])

with tab1:
    st.subheader("Research Data")
    research_query = st.text_area("Enter your research question:")
    if st.button("Get Research Data", key="research"):
        if research_query:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=f"Research data on: {research_query}"
            )
            st.write(response.text)

with tab2:
    st.subheader("Summary")
    summary_input = st.text_area("Paste text to summarize:")
    if st.button("Generate Summary", key="summary"):
        if summary_input:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=f"Summarize this text: {summary_input}"
            )
            st.write(response.text)

with tab3:
    st.subheader("Draft Email")
    email_prompt = st.text_area("Enter your instructions for email:")
    if st.button("Generate Email", key="email"):
        if email_prompt:
            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=f"Write a professional email: {email_prompt}"
            )
            st.write(response.text)
