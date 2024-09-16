#Importing LLM Model Llama 3
from llama_index.llms.ollama import Ollama # pip install llama-index-llms-ollama
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, StorageContext
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core.response.pprint_utils import pprint_source_node
import streamlit as st
    
#Embed Model
def embedModel():
    from llama_index.embeddings.fastembed import FastEmbedEmbedding # pip install llama-index-embeddings-fastembed

    MAKE SURE TO REMOVE CACHE FOR EMBED MODEL - RUN COMMENTED TERMINAL LINE
    Settings.embed_model = FastEmbedEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2") # rm -rf /var/folders/w9/2rlrrdw13xdff2m0rn934ql80000gp/T/fastembed_cache
    print("embedding model successfull")


def LLMModel():
    Settings.llm = Ollama(model="llama3", request_timeout=3600) # pip install --upgrade llama-index llama-index-llms-ollama
    print("Ollama model instaniated successfully")

YOU WILL NEED TO CREATE A PINECONE ACCOUNT AND LINK AN API KEY
#Embed loaded data with VectorStoreIndex and store in PineCone Vector Store
def query(question):
    from llama_index.core import SimpleDirectoryReader # pip install llama-index


RUN THE LOADING AND STORING VECTORS INTO VECTOR STORE CODE BELOW THE FIRST TIME WITH YOUR PINECONE API KEY

    CREATE A FOLDER IN YOUR WORK DIRECTORY CALLED 'data'  AND UPLOAD PDF DOCUMENTS OF HISTORY BOOKS
    #reader = SimpleDirectoryReader("./data") # , file_extractor=file_extractor
    #documents = reader.load_data()
    #print("Data loaded successfully")

    #PineCone
    pc = Pinecone(api_key= YOUR PINECONE API KEY)


    # Delete the existing index
    #pc.delete_index("history-info")
    #print("Existing index 'history-info' deleted.")


    #pc.create_index(
        #name="history-info",
        #dimension=384,
        #metric="cosine",
        #spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    #)

    pinecone_index = pc.Index("history-info")

    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)


RUN STREAMLIT COMMAND ON TERMINAL: 
pip install streamlit
streamlit run YOURFILENAME.py  (Use url given to see chat bot on webpage, works better on chrome browser)


#define streamlit
st.title("History ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter Question")
if prompt:
    #st.write(prompt)
    def st_bot(prompt):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
        
        #get answer from LLM
        embedModel()
        LLMModel()
        resp = query(prompt)
                
        with st.chat_message("assistant"):
            st.markdown(resp)

        st.session_state.messages.append({"role": "assistant", "content": resp})

    st_bot(prompt)

