import streamlit as st
#from llama_index.llms.gemini import Gemini
#from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
#from llama_index.embeddings.gemini import GeminiEmbedding
import google.generativeai as genai

GOOGLE_API_KEY= st.secrets.google_gemini_key
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Return Multiple Responses", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Return Multiple Responses")



with st.form("my_form"):
    st.write("Inside the form")
    temp_val = st.slider("Temperature", min_value=0.0, max_value=2.0, step=.1)
    topk_val = st.slider("Tokens Considered", min_value=1, max_value=200, step=1)
    topp_val = st.slider("Top P", min_value=0.0, max_value=1.0, step=0.05)
    text_val = st.text_area("Query")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        #st.write("temperature", temp_val, "query", text_val, "tokens considered", topk_val) 
        #llm = Gemini(model="models/gemini-1.5-flash", api_key=st.secrets.google_gemini_key, temperature=temp_val, topK = topk_val, topP = 1.0)
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
            generation_config=genai.GenerationConfig(
            max_output_tokens=2000,
            temperature=temp_val,
            topK=topk_val,
            topP=topp_val,
        ))
        i = 0
        while i < 11:
            #resp = llm.complete(text_val)
            resp = model.generate_content(text_val)
            st.write(resp.text)
            i +=1

st.write("Outside the form")


