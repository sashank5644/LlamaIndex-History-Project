This project is built in python and based on the principles of retreival augmented generation (RAG) and is used to curate answers to querys about topics of history. The data was collected from valid
open to use history textbooks from openstax, and gutenberg. 

To build the system, the LlamaIndex framework was used along with a local large language model (LLM) from Ollama LLMs. To collect the data and transform it into documents, and embed and store the information
the LlamaIndex tools were used such as SimpleDirectoryReader, VectorStoreIndex, and PineCone Vector Store. 

The querying of information was done with LlamaIndex through a query engine which can use the data collected and given to systhesise and curate an accurate response to a question asked by the user.

--------- Code ------------

The code was done in Python with tools from LlamaIndex and local Ollama based LLM model llama 3.

To run the code you will need to install Ollama through their website, and follow the instruction on the LlamaIndex RAG Code documentation.
