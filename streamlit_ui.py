import streamlit as st
from api import run_agent

st.set_page_config(page_title="🤖 Agent Orchestration", layout="wide")

st.title("🤖 Agent Orchestration")

tabs = st.tabs(["Research", "Summary", "Email"])

def render_tab(task_name, system_prompt):
    with st.container():
        st.subheader(f"{task_name} Agent")

        text = st.text_area(
            "Enter your text",
            height=200,
            key=f"text_{task_name}"
        )

        if st.button("Run", key=f"btn_{task_name}"):
            with st.spinner("Running agent..."):
                output = run_agent(system_prompt, text)

            st.success(f"{task_name} agent executed successfully!")
            st.markdown("### Output:")
            st.write(output)

with tabs[0]:
    render_tab("Research", "You are a research assistant.")

with tabs[1]:
    render_tab("Summary", "Summarize the following text.")

with tabs[2]:
    render_tab("Email", "Write a professional email.")
