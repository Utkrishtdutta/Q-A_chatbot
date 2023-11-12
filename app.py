import streamlit as st
from langchain.llms import OpenAI

with st.sidebar:
    openai_api_key = st.text_input('Enter your openai API key',type='password')


def open_ai_response(question,openai_api_key):
    try:
        llm = OpenAI(model_name="text-davinci-003",temperature=0.5,openai_api_key = openai_api_key)
        response = llm(question)
        return response
    except:
       st.error('Please Check your API Key', icon="🚨")
       st.stop()


st.title('Q&A ChatBot')
st.subheader("Langchain Application")
question  = st.text_input('Ask your question')
submit = st.button('Submit')
if not openai_api_key:
    st.warning("Please put OpenAi key to continue.",icon="⚠️")
    st.stop()
response = open_ai_response(question,openai_api_key)

if submit:
    st.subheader('The Response is :- ')
    st.text(response)


