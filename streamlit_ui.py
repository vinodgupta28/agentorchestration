import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Agent Orchestration",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🤖 Agent Orchestration")
st.caption("Research • Summary • Email Automation")

st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([" Research", " Summary", " Email"])

def render_tab(tab_name):
    st.subheader(f"{tab_name} Agent")

    text = st.text_area(
        "Enter your text",
        height=220,
        key=f"text_{tab_name}"   
    )

    if st.button("Run", key=f"run_{tab_name}"):
        if text.strip() == "":
            st.warning("Please enter some text first.")
        else:
            st.success(f"{tab_name} agent executed successfully!")
            st.write("### Output:")
            st.write(text)  # later yahan agent output aayega

# ---------------- TAB CONTENT ----------------
with tab1:
    render_tab("Research")

with tab2:
    render_tab("Summary")

with tab3:
    render_tab("Email")
