import streamlit as st
import google.generativeai as genai

#Get API Key
GOOGLE_API_KEY= st.secrets.google_gemini_key
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="10x Chatbot", page_icon="🐇", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("10x Chatbot")
st.write("This application queries Google Gemini ten times for each prompt. This can be helpful in demonstrating the effects of temperature and other parameters that control randomness. The different controls interact with one another - try moving all three all the way to the right to see the most randomness.")
st.write("<center>&larr; Less Random ---- More Random &rarr;</center>", unsafe_allow_html="true")

#create a form
with st.form("my_form"):
    #form controls for temperature, topK, topP, and query
    temp_val = st.slider("Temperature", help="Temperature controls the degree of randomness in token selection. Temperature only has an effect when the other parameters are set to allow more than one token to be considered.", min_value=0.0, max_value=2.0, step=.1)
    topk_val = st.slider("Tokens Considered (Top-K)", help="Tokens considered (top-K) changes how the model selects possible tokens. A top-K of 1 means the model will only consider the most probable among all tokens in the model's vocabulary, while a top-K of 3 means that each token is selected from among the three most probable tokens.", min_value=1, max_value=100, step=1) 
    topp_val = st.slider("Threshold for Consideration (Top-P)", help="Top-P changes how the model selects tokens for output. Tokens are selected from the most (see top-K) to least probable until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-P value is 0.5, then the model will select either A or B as the next token by using temperature and excludes C as a candidate. For many queries, you will not see much randomness until you increase top-p to 1.0.",min_value=0.0, max_value=1.0, step=0.05)
    text_val = st.text_area("Query")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # set LLM parameters
        model = genai.GenerativeModel(
            'gemini-1.5-flash',
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



