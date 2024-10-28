import streamlit as st
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.gemini import GeminiEmbedding


st.set_page_config(page_title="Return Multiple Responses", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Return Multiple Responses")

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Temperature", max_value=1.0, step=.1)
    text_val = st.text_area("Query")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "query", text_val, "checkbox", checkbox_val)
st.write("Outside the form")


