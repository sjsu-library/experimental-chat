import streamlit as st
from llama_index.llms.gemini import Gemini
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.gemini import GeminiEmbedding


st.set_page_config(page_title="Return Multiple Responses", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Return Multiple Responses")




@st.cache_resource(show_spinner=False)
def load_data():

    Settings.llm = Gemini(
        model="models/gemini-1.5-flash",
        temperature=0.2,
        api_key = st.secrets.google_gemini_key,
        safe = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
],
    )
 

if "chat_engine" not in st.session_state.keys():  # Initialize the chat engine
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode="condense_plus_context", verbose=True, streaming=False,
    )

if prompt := st.chat_input(
    "Ask a question"
):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:  # Write message history to UI
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response_stream = ""
        try:
            response_stream = st.session_state.chat_engine.stream_chat(prompt)
        except:
            st.error("We got an error from Google Gemini - this may mean the question had a risk of producing a harmful response. Consider asking the question in a different way.")        
        if response_stream != "":
            with st.spinner("waiting"):
                try:
                    st.write_stream(response_stream.response_gen)
                except:
                    st.error("We hit a bump - let's try again")
                    try:
                        resp = st.session_state.chat_engine.chat(prompt)[0]
                        st.write(resp)
                    except:
                        st.error("We got an error from Google Gemini - this may mean the question had a risk of producing a harmful response. Consider asking the question in a different way.")
            message = {"role": "assistant", "content": response_stream.response}
            # Add response to message history
            st.session_state.messages.append(message)
