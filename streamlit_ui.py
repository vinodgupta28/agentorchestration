import streamlit as st
import os

def run_multi_agent_workflow(topic):
    # Dummy example — replace with real agent logic
    return {
        "research": [f"Research result for: {topic}"],
        "critic": f"Critic review for: {topic}",
        "sources": [{"title": "Example Source", "url": "https://example.com"}],
        "fact_check": f"Fact check for: {topic}",
        "insights": [f"Insight 1 about {topic}", f"Insight 2 about {topic}"],
        "summary": f"Summary of {topic}",
        "email": {"text": f"Email draft regarding {topic}"},
        "titles": [f"Title suggestion for {topic}"]
    }

def normalize_text(data):
    if data is None:
        return ""

    # If already string → return directly
    if isinstance(data, str):
        return data

    # If list → convert to paragraphs safely
    if isinstance(data, list):
        clean = []
        for item in data:
            if isinstance(item, dict):
                clean.append("\n".join([f"**{k}**: {v}" for k, v in item.items()]))
            else:
                clean.append(str(item))
        return "\n\n".join(clean)

    # If dict → readable sections
    if isinstance(data, dict):
        if "text" in data and isinstance(data["text"], str):
            return data["text"]

        sections = []
        for k, v in data.items():
            sections.append(f"### {k.capitalize()}\n{normalize_text(v)}")
        return "\n\n".join(sections)

    # fallback
    return str(data)

def format_output(data):
    """
    Converts dict/list output to readable text for Streamlit.
    """
    if isinstance(data, dict):
        # Join key-values as text
        return "\n\n".join([f"**{k}**: {v}" for k, v in data.items()])
    elif isinstance(data, list):
        # Join list items as paragraphs
        return "\n\n".join([str(item) for item in data])
    else:
        return str(data)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Groq Multi-Agent Research System",
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
st.markdown('<h1 class="header-text">🤖 Groq Multi-Agent Research System</h1>', unsafe_allow_html=True)
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
    with st.spinner("Groq agents collaborating..."):
        output = run_multi_agent_workflow(topic)


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

    # ---------------- TAB CONTENT ----------------
    with tabs[0]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)

        research_raw = output.get("research")

        if research_raw:
            research_text = normalize_text(research_raw)
            st.markdown(research_text)
        else:
            st.info("No research output available.")

        st.markdown("</div>", unsafe_allow_html=True)


        st.markdown(research_text)
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[1]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output.get("critic", "No critic output available."))
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[2]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        sources = output.get("sources", [])
        normalized_sources = []
        if isinstance(sources, dict):
            for k, v in sources.items():
                normalized_sources.append({"title": k, "url": v})
        elif isinstance(sources, list):
            for s in sources:
                if isinstance(s, dict):
                    normalized_sources.append(s)
                else:
                    normalized_sources.append({"title": str(s), "url": str(s)})

        if normalized_sources:
            for s in normalized_sources:
                st.markdown(f"- [{s['title']}]({s['url']})")
        else:
            st.info("No sources available for this topic.")


    with tabs[3]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output.get("fact_check", "No fact check output available."))
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[4]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown(format_output(output.get("insights", "No insights available.")))
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- Summary ----------------
    with tabs[5]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown(format_output(output.get("summary", "No summary available.")))
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[6]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        email_output = output.get("email", "")
        email_text = email_output.get("text", "") if isinstance(email_output, dict) else email_output
        st.markdown(email_text or "No email output available.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tabs[7]:
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.write(output.get("titles", "No titles available."))
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

# ---------------- HANDLE EMPTY INPUT ----------------
elif run:
    st.warning("⚠️ Please enter a topic")
