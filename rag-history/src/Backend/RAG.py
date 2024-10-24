#Importing LLM Model Llama 3
#pip install Flask llama-index llama-index-llms-ollama pinecone
from flask import Flask, jsonify, request # pip install Flask
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
from MongoDB import store_chat_message, get_chat_history, delete_chat_message
    
app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

#System Prompt
SYSTEM_PROMPT = "You are a historian that will give evidence based answers from the text about history and not use phrases such as 'according to the text' and you will not answer question unrelated to history."


#Embed Model
def embedModel():
    from llama_index.embeddings.fastembed import FastEmbedEmbedding # pip install llama-index-embeddings-fastembed
    Settings.embed_model = FastEmbedEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2") # rm -rf /var/folders/w9/2rlrrdw13xdff2m0rn934ql80000gp/T/fastembed_cache
    print("embedding model successfull")


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


    #If you are running for the first time / did not store embeddings in vector store
    reader = SimpleDirectoryReader("./data") 
    documents = reader.load_data()
    print("Data loaded successfully")
    #If you are running for the first time / did not store embeddings in vector store


    #PineCone
    pc = Pinecone(api_key="YOUR API KEY HERE")


    # Delete the existing index
    #pc.delete_index("history-info")
    #print("Existing index 'history-info' deleted.")


    #If you are running for the first time / did not store embeddings in vector store
    pc.create_index(
        name="history-info",
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    #If you are running for the first time / did not store embeddings in vector store


    pinecone_index = pc.Index("history-info")

    vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)


    #If you are running for the first time / did not store embeddings in vector store
    vector_index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        show_progress=True,     
    )
    #If you are running for the first time / did not store embeddings in vector store
    

    #If embeddings already stored in vector store
    #vector_index = VectorStoreIndex.from_vector_store(
        #vector_store=vector_store,
        #storage_context=storage_context,
        #show_progress=True,     
    #)
    #If embeddings already stored in vector store


    #retriever
    retriever = VectorIndexRetriever(
        index = vector_index,
        similarity_top_k = 4,
    )

    #response synthsizer
    response_synthesizer = get_response_synthesizer()

    #query engine
    query_engine = RetrieverQueryEngine(
        retriever = retriever,
        response_synthesizer = response_synthesizer,
        node_postprocessors = [SimilarityPostprocessor(similarity_cutoff=0.7)],
    )

    print("Index retrieved from vector store")

    #Answer Query
    query_engine = vector_index.as_query_engine()
    full_prompt = f"{SYSTEM_PROMPT}\n\n{question}"
    response = query_engine.query(full_prompt)
    return str(response)
    #print(response)

@app.route('/query', methods=['POST'])
def handle_query():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = app.make_default_options_response()
        return response
        
    question = request.json.get('question')
    user_id = request.json.get('user_id')

    response = query(question)
    store_chat_message(user_id, question, str(response))

    return jsonify({"response": response})

@app.route('/chat_history', methods=['GET'])
def get_user_chat_history():
    user_id = request.args.get('user_id')
    history = get_chat_history(user_id)
    return jsonify(history)

@app.route('/chat_history/<message_id>', methods=['DELETE'])
def delete_chat(message_id):
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    success = delete_chat_message(message_id, user_id)
    if success:
        return jsonify({"message": "Chat message deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete chat message"}), 404
    
if __name__ == '__main__':
    embedModel()
    LLMModel()
    app.run(debug=True)


