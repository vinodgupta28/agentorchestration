import streamlit as st
import os

# Try to import backend directly
from app import run_agents

# Optional: requests only if local FastAPI is needed
import requests

# -----------------------------
# Streamlit App Configuration
# -----------------------------
st.set_page_config(page_title="Agent Orchestration", page_icon="", layout="wide")

# FORCE LIGHT THEME USING CSS
st.markdown("""
<style>
.stApp { background-color: #ffffff; color: #000000; }
input, textarea { background-color: #ffffff !important; color: #000000 !important; border: 1px solid #d1d5db !important; }
.stButton > button { background-color: #2563eb; color: white; border-radius: 6px; padding: 8px 20px; }
button[data-baseweb="tab"] { background-color: #f3f4f6; color: black; border-radius: 6px; margin-right: 6px; }
button[data-baseweb="tab"][aria-selected="true"] { background-color: #2563eb; color: white; }
header, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# TITLE AND SUBTITLE
st.markdown("<h1 style='text-align:center;'>Agent Orchestration Framework</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Research → Summarise → Email using LangChain & Gemini</p>", unsafe_allow_html=True)

# -----------------------------
# User Input Section
# -----------------------------
topic = st.text_input("What would you like to research?", placeholder="Describe the Transformer architecture paper")
start = st.button("Start Research")

# -----------------------------
# Determine if running locally or on Cloud
# -----------------------------
USE_LOCAL_API = st.checkbox("Use local FastAPI (127.0.0.1)", value=False)

# -----------------------------
# Process Backend & Show Tabs
# -----------------------------
if start:
    if topic.strip() == "":
        st.warning("Please enter a topic first")
    else:
        with st.spinner("Agents are working..."):
            try:
                if USE_LOCAL_API:
                    # Call local FastAPI endpoint
                    response = requests.post(
                        "http://127.0.0.1:8000/run-agents",
                        json={"topic": topic},
                        timeout=60
                    )
                    data = response.json()
                else:
                    # Call backend directly (Streamlit Cloud friendly)
                    data = run_agents(topic)

                # Display results in tabs
                tab1, tab2, tab3 = st.tabs(["Research", "Summary", "Email"])

                with tab1:
                    st.subheader("Research Output")
                    st.write(data.get("research", "No research output"))

                with tab2:
                    st.subheader("Summary Output")
                    st.write(data.get("summary", "No summary output"))

                with tab3:
                    st.subheader("Email Draft")
                    st.write(data.get("email", "No email output"))

            except Exception as e:
                st.error(f"Backend error: {e}")
