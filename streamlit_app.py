import streamlit as st
import google.generativeai as genai

#Get API Key
GOOGLE_API_KEY= st.secrets.google_gemini_key
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="Return Multiple Responses", page_icon="🐇", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Return Multiple Responses")


#create a form
with st.form("my_form"):
    #form controls for temperature, topK, topP, and query
    temp_val = st.slider("Temperature", min_value=0.0, max_value=2.0, step=.1)
    topk_val = st.slider("Tokens Considered", min_value=1, max_value=100, step=1)
    topp_val = st.slider("Top P", min_value=0.0, max_value=1.0, step=0.05)
    text_val = st.text_area("Query")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # set LLM parameters
        model = genai.GenerativeModel(
            'gemini-2.5-flash',
            generation_config={'max_output_tokens':100,'temperature':temp_val,'top_k':topk_val,'top_p':topp_val }
        )
        i = 0
        #loop 10 times
        while i < 10:
            #get response from LLM
            resp = model.generate_content(text_val)
            #write response to the page - need to add error catching here for harmful content
            st.write(resp.text)
            st.divider()
            i +=1



