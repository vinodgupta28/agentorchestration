import streamlit as st
import requests

# FORCE LIGHT MODE (NO EXTRA FILE)
st.set_page_config(
    page_title="Agent Orchestration Framework",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# FORCE LIGHT THEME USING CSS ONLY
st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #ffffff;
    color: #000000;
}

/* Input box */
input, textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #d1d5db !important;
}

/* Button */
.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 6px;
    padding: 8px 20px;
}

/* Tabs */
button[data-baseweb="tab"] {
    background-color: #f3f4f6;
    color: black;
    border-radius: 6px;
    margin-right: 6px;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #2563eb;
    color: white;
}

/* Remove Streamlit dark leftovers */
header, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("<h1 style='text-align:center;'>Agent Orchestration Framework</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;'>Research → Summarise → Email using LangChain & Gemini</p>",
    unsafe_allow_html=True
)

# INPUT
topic = st.text_input(
    "What would you like to research?",
    placeholder="Describe the Transformer architecture paper"
)

start = st.button("Start Research")

# RESULT
if start:
    if topic.strip() == "":
        st.warning("Please enter a topic first")
    else:
        with st.spinner("Agents are working..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/run",
                    json={"topic": topic},
                    timeout=60
                )

                data = response.json()

                tab1, tab2, tab3 = st.tabs(
                    [" Research", " Summary", " Email"]
                )

                with tab1:
                    st.subheader("Research Output")
                    st.write(data["research"])

                with tab2:
                    st.subheader("Summary Output")
                    st.write(data["summary"])

                with tab3:
                    st.subheader("Email Draft")
                    st.write(data["email"])

            except Exception as e:
                st.error(f"Backend error: {e}")
