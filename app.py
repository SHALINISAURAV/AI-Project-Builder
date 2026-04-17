import streamlit as st
from agents.planner import planner
from agents.code_generator import generate_code
from agents.reviewer import review_code
from agents.explainer import explain_code

st.set_page_config(page_title="AI Project Builder", layout="wide")

st.title("🚀 AI Project Builder")

user_input = st.text_input("💡 Enter your project idea")

if st.button("Build Project"):
    with st.spinner("⚡ AI is building your project..."):
        plan = planner(user_input)
        code = generate_code(plan)
        reviewed = review_code(code)
        explanation = explain_code(reviewed)

    tab1, tab2, tab3, tab4 = st.tabs(["📌 Plan", "💻 Code", "✅ Improved", "📖 Explain"])

    with tab1:
        st.write(plan)

    with tab2:
        st.code(code)

    with tab3:
        st.code(reviewed)

    with tab4:
        st.write(explanation)
        
        st.download_button(
    label="⬇ Download Final Code",
    data=reviewed,
    file_name="project.py"
)
