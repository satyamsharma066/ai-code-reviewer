import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Code Reviewer", page_icon="💻", layout="wide")
st.title("💻 AI Code Reviewer & Bug Fixer")
st.markdown("Paste your Python, C++, or JS code below. The AI will find bugs, fix errors, and suggest improvements.")

st.sidebar.header("Configuration")
st.sidebar.markdown("Please enter your Free Google Gemini API Key to run this app.")
api_key = st.sidebar.text_input("Enter your Gemini API Key here:", type="password")
st.sidebar.markdown("*(Get your free key from [Google AI Studio](https://aistudio.google.com/app/apikey))*")

code_input = st.text_area("Paste your code here:", height=300)

if st.button("Review My Code"):
    if not api_key:
        st.error("⚠️ Please enter your API Key in the sidebar first.")
    elif not code_input.strip():
        st.warning("⚠️ Please paste some code to review.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = f"""
            You are an expert AI code reviewer. Please review the following code:
            1. Identify any bugs or errors.
            2. Suggest improvements for better performance or readability.
            3. Provide the corrected/improved version of the code.
            
            Code:
            {code_input}
            """
            
            with st.spinner("Analyzing code..."):
                response = model.generate_content(prompt)
                
            st.subheader("🤖 AI Review & Feedback:")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
