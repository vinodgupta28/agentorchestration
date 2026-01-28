import streamlit as st
from app import orchestrator
import os

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
    font-size: 2.5rem;
    font-weight: bold;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
}
.hero-image {
    height: 100px;
    object-fit: cover;
    width: 25%;
}
.css-18e3th9 {
    background-color: transparent;
}
.main { background-color: #f7f9fc; }
.block-container { padding-top: 2rem; }
.hero {
    background: linear-gradient(90deg, #eef2ff, #f8fafc);
    padding: 30px;
    border-radius: 16px;
    margin-bottom: 30px;
}
.section {
    background-color: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<h1 class="header-text">🤖 Gemini Multi-Agent Research System</h1>', unsafe_allow_html=True)
st.markdown('<p class="header-text">Research • Critic • Fact-Check • Insights • Summary • Email</p>', unsafe_allow_html=True)

# ---------------- HERO IMAGE ----------------
local_image_path = "72958382-f2d4-4007-a898-2330db6650b9.png"

if os.path.exists(local_image_path):
    st.image(local_image_path, use_column_width=True, output_format="PNG")
else:
    # Fallback online image
    st.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995",
        use_column_width=True,
        caption="AI-powered Multi-Agent Orchestration"
    )

# ---------------- INPUT SECTION ----------------
with st.container():
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
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(
                "https://images.unsplash.com/photo-1550751827-4bd374c3f58b",
                width=500,
                caption="Multi-Agent AI Collaboration"
            )
        st.info("🧠 Visual representation of agent collaboration (Gemini Vision ready)")
        st.markdown("</div>", unsafe_allow_html=True)

elif run:
    st.warning("⚠️ Please enter a topic")
