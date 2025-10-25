import streamlit as st
import requests

# Title
st.set_page_config(page_title="AI Text Summarizer", page_icon="🧠", layout="wide")
st.title("🧠 AI Text Summarizer")
st.markdown("Enter your text below and get a concise summary instantly!")

# Input area
input_text = st.text_area("✍️ Paste your text here", height=200, placeholder="Type or paste a long paragraph...")

# Summarize button
if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            try:
                # Change this to your FastAPI endpoint
                response = requests.post("http://127.0.0.1:8000/predict", json={"text": input_text})
                
                if response.status_code == 200:
                    summary = response.json().get("summary", "")
                    st.success("✅ Summary generated successfully!")
                    st.text_area("🧾 Summary:", summary, height=200)
                else:
                    st.error("Error: Unable to generate summary. Please check your API.")
            except Exception as e:
                st.error(f"⚠️ Server error: {e}")

# Footer
st.markdown("---")
st.markdown("💡 *Built with Streamlit and FastAPI*")
