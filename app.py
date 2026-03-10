import streamlit as st

st.title("RAG Website Chatbot")

url = st.text_input("Enter Website URL")

if st.button("Process Website"):
    st.write("Scraping website...")

question = st.chat_input("Ask question")

if question:
    st.write("Answer coming soon...")