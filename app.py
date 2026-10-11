import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Code Reviewer", page_icon="💻", layout="wide")
st.title("💻 AI Code Reviewer & Bug Fixer")
st.markdown("Paste your Python, C++, or JS code below. The AI will find bugs, fix errors, and suggest improvements.")

st.sidebar.header("Configuration")
st.sidebar.markdown("Is app ko chalane ke liye ek Free Google Gemini API Key chahiye.")
api_key = st.sidebar.text_input("Enter your Gemini API Key here:", type="password")
st.sidebar.markdown("*(Get your free key from [Google AI Studio](https://aistudio.google.com/app/apikey))*")

code_input = st.text_area("Apna code yahan paste karo:", height=300)

if st.button("Review My Code"):
    if not api_key:
        st.error("⚠️ Please enter your API Key in the sidebar first.")
    elif not code_input.strip():
        st.warning("⚠️ Please paste some code to review.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            
            prompt = f"You are an expert Code Reviewer. Analyze the following code carefully.\n1. Identify any bugs and syntax errors.\n2. Suggest better ways to write it (clean code / optimization).\n3. Provide the final corrected code.\n\nHere is the code to review:\n{code_input}"
            
            with st.spinner("AI tumhara code check kar raha hai... Please wait."):
                response = model.generate_content(prompt)
                
            st.success("Analysis Complete!")
            st.markdown("### Output:")
            st.markdown("---")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"❌ Kuch error aa gaya. API key check karo. Error: {e}")