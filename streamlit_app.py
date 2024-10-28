import streamlit as st
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.gemini import GeminiEmbedding


st.set_page_config(page_title="Return Multiple Responses", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Return Multiple Responses")



with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Temperature", min_value=0.0, max_value=1.0, step=.1)
    text_val = st.text_area("Query")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("temperature", slider_val, "query", text_val) 
        llm = Gemini(model="models/gemini-1.5-flash", api_key=st.secrets.google_gemini_key, temperature=slider_val, system_prompt="Keep your response short")
        i = 0
        while i < 11:
            resp = llm.complete(text_val)
            st.write(resp.text)
            i +=1

st.write("Outside the form")


