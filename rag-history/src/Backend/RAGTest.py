#Importing LLM Model Llama 3
#pip install Flask llama-index llama-index-llms-ollama pinecone
from flask import Flask, request # pip install Flask
from flask_cors import CORS #pip install flask-cors
from llama_index.llms.ollama import Ollama # pip install llama-index-llms-ollama
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, StorageContext, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore # pip install llama-index-vector-stores-pinecone
from llama_index.core.response.pprint_utils import pprint_source_node
    
app = Flask(__name__)
CORS(app)

#System Prompt
SYSTEM_PROMPT = "You are a historian that will give evidence based answers from the text about history and not use phrases such as 'according to the text' and you will not answer question unrelated to history."


#Embed Model
def embedModel():
    from llama_index.embeddings.fastembed import FastEmbedEmbedding # pip install llama-index-embeddings-fastembed
    Settings.embed_model = FastEmbedEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2") # rm -rf /var/folders/w9/2rlrrdw13xdff2m0rn934ql80000gp/T/fastembed_cache
    print("embedding model successfull")

#LLM Model (Ollama Llama 3)
def LLMModel():
    Settings.llm = Ollama(model="llama3", 
        request_timeout=3600, 
        top_k = 3,
        tok_p = 0.6,
        temperature = 0.5,
    )
    print("Ollama model instaniated successfully")


#Embed loaded data with VectorStoreIndex and store in PineCone Vector Store
def query(question):
    from llama_index.core import SimpleDirectoryReader # pip install llama-index

    reader = SimpleDirectoryReader("./Test Data")
    documents = reader.load_data()
    print("Data loaded successfully")
    
    vector_index = VectorStoreIndex.from_documents(
        documents,
        show_progress=True,     
    )

    #retriever
    retriever = VectorIndexRetriever(
        index = vector_index,
        similarity_top_k = 4,
    )

    #response synthsizer
    response_synthesizer = get_response_synthesizer()

    #Answer Query
    query_engine = vector_index.as_query_engine()
    full_prompt = f"{SYSTEM_PROMPT}\n\n{question}"
    response = query_engine.query(full_prompt)
    return str(response)

@app.route('/query', methods=['POST'])
def handle_query():
    question = request.json.get('question')
    response = query(question)
    return response

if __name__ == '__main__':
    embedModel()
    LLMModel()
    app.run(debug=True)


