### Building End To End LLM And Large Image Model Application Uing Gemini Pro

from dotenv import load_dotenv
load_dotenv()  # loading the env variables
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a function to load Gemini Pro model and get responses
model=genai.GenerativeModel(model_name="gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

# Initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input:",key="input")
submit=st.button("Ask a question")

# if ask button is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)