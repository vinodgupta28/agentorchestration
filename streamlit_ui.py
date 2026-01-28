import streamlit as st
from app import orchestrator

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gemini Multi-Agent Research System",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.header-text {
    color: black;
    font-size: 2.2rem;
    font-weight: bold;
}
.sub-text {
    font-size: 1rem;
    color: #444;
    margin-bottom: 10px;
}
.main { background-color: #f7f9fc; }
.block-container { padding-top: 1.5rem; }

.section {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 class='header-text'>🤖 Gemini Multi-Agent Research System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='sub-text'>Research • Critic • Fact-Check • Insights • Summary • Email</p>",
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION (NO SCROLL) ----------------
st.markdown("<div class='section'>", unsafe_allow_html=True)

topic = st.text_input(
    "🔎 Enter Research Topic",
    placeholder="What is Artificial Intelligence?"
)

run = st.button("🚀 Start Research")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RUN AGENTS ----------------
if run and topic.strip():
    with st.spinner("🤝 Gemini agents collaborating..."):
        output = orchestrator(topic)

    tabs = st.tabs([
        "🔍 Research",
        "🧠 Critic Review",
        "🔗 Sources",
        "✅ Fact Check",
        "📊 Insights",
        "📄 Summary",
        "✉️ Email",
        "🏷️ Titles",
        "🖼 Visual"
    ])

    with tabs[0]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["research"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["critic"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        for s in output["sources"]:
            st.markdown(f"- [{s['title']}]({s['url']})")
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[3]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["fact_check"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[4]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["insights"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[5]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["summary"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[6]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        email_output = output["email"]
        email_text = email_output.get("text", "") if isinstance(email_output, dict) else email_output
        st.markdown(email_text)
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[7]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output["titles"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[8]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
            width=400,
            caption="Multi-Agent AI Collaboration"
        )
        st.markdown("</div>", unsafe_allow_html=True)

elif run:
    st.warning("⚠️ Please enter a topic")
