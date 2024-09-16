This project is built in python and based on the principles of retreival augmented generation (RAG) and is used to curate answers to querys about topics of history. The data was collected from valid
open to use history textbooks from openstax, and gutenberg. 

To build the system, the LlamaIndex framework was used along with a local large language model (LLM) from Ollama LLMs. To collect the data and transform it into documents, and embed and store the information
the LlamaIndex tools were used such as SimpleDirectoryReader, VectorStoreIndex, and PineCone Vector Store. 

The querying of information was done with LlamaIndex through a query engine which can use the data collected and given to systhesise and curate an accurate response to a question asked by the user.

--------- Code ------------

The code was done in Python with tools from LlamaIndex and local Ollama based LLM model llama 3.

To run the code you will need to install Ollama through their website, and follow the instruction on the LlamaIndex RAG Code documentation.

Installation

    pip install llama-index-llms-ollama
    pip install llama-index-embeddings-fastembed
    pip install --upgrade llama-index llama-index-llms-ollama
    pip install llama-index
        

Prerequisites

Go to PineCone ("https://login.pinecone.io/login?state=hKFo2SBoM3RvdXkyWGJEWnFqSmRvbXNYVVFMdnplM2NhRHpFQaFupWxvZ2luo3RpZNkgZkZrQU9XemJkblZjQjRpbWNJbVlWTUZpMGV0ZmtNemKjY2lk2SBUOEkyaEc2Q2FaazUwT05McWhmN3h6a1I0WmhMcVM0Qw&client=T8I2hG6CaZk50ONLqhf7xzkR4ZhLqS4C&protocol=oauth2&audience=https%3A%2F%2Fus-central1-production-console.cloudfunctions.net%2Fapi%2Fv1&scope=openid%20profile%20email%20read%3Acurrent_user&redirect_uri=https%3A%2F%2Fapp.pinecone.io&sessionType=signup&response_type=code&response_mode=query&nonce=LUlWMzdPMTZUc1FYTjZ1Y013UUlYWDZ1TnhJWU5MazZsY2V5bXhfcFl0bw%3D%3D&code_challenge=GixqfohLLF_k5DAU_hLAG-MrTkreLKKRZxUaUl8HdWU&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4xMi4xIn0%3D") and create an API Key.
