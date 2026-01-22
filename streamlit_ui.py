import streamlit as st
from api import run_multi_agent

st.set_page_config(page_title="🤖 Agent Orchestration", layout="wide")

st.title("🤖 Agent Orchestration ")
st.caption(" Research → Summary → Email")

topic = st.text_area(
    "Enter topic",
    height=120
)

if st.button("Run "):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Agents thinking with memory..."):
            memory = run_multi_agent(topic)

        tab1, tab2, tab3 = st.tabs([" Research", " Summary", " Email"])

        with tab1:
            st.text_area("Research", memory["research"], height=350)

        with tab2:
            st.text_area("Summary", memory["summary"], height=250)

        with tab3:
            st.text_area("Email", memory["email"], height=250)
