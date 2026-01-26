import streamlit as st
from api import run_multi_agent_workflow

st.set_page_config(
    page_title="LangChain Multi-Agent Orchestration",
    layout="wide"
)

st.title("🤖 LangChain Multi-Agent Orchestration System")
st.caption("Research → Critic → Summary → Email → Images")

st.divider()

topic = st.text_area(
    "📌 Enter Topic",
    placeholder="Enter topic once. All agents will run automatically...",
    height=100
)

run = st.button("🚀 Run Agents")


# 🔥 helper function to clean agent output
def clean_output(output):
    if isinstance(output, list):
        # Gemini / LangChain structured response case
        return output[0].get("text", "")
    return output


if run and topic.strip():

    with st.status("Running multi-agent workflow...", expanded=True):
        outputs = run_multi_agent_workflow(topic)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🔍 Research", "🧪 Critic", "📝 Summary", "✉️ Email", "🖼 Images"]
    )

    with tab1:
        st.subheader("Research Output")
        st.markdown(clean_output(outputs["research"]))

    with tab2:
        st.subheader("Critic Review")
        st.markdown(clean_output(outputs["critic"]))

    with tab3:
        st.subheader("Summary")
        st.markdown(clean_output(outputs["summary"]))

    with tab4:
        st.subheader("Professional Email")
        st.markdown(clean_output(outputs["email"]))

    with tab5:
        st.subheader("Images")
        st.image(
            "https://via.placeholder.com/400x250.png?text=AI+Image+Agent",
            caption="Future Image Agent"
        )

elif run:
    st.warning("⚠️ Please enter a topic")
