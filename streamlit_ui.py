import streamlit as st
from api import run_agent

st.set_page_config(page_title="🤖 Agent Orchestration", layout="wide")

st.title("🤖 Agent Orchestration")

tab1, tab2, tab3 = st.tabs(["Research", "Summary", "Email"])

with tab1:
    st.header("Research Agent")
    text = st.text_area("Enter your text", key="research")

    if st.button("Run Research"):
        with st.spinner("Researching..."):
            output = run_agent("research", text)

        st.success("Research agent executed successfully!")
        st.subheader("Output:")
        st.write(output)
