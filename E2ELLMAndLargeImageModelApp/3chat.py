from dotenv import load_dotenv
load_dotenv()  # loading the env variables
import os
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a function to load Gemini Pro model and get responses
model=genai.GenerativeModel(model_name="gemini-pro")
chat=model.start_chat(history=[]) 
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input:",key="input")
submit=st.button("Ask a question")

# if ask button is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    st.write(chat.history)