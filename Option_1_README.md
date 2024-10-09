# Option 1

**Option 1**: Running the Retreival-Augmented Generation (RAG) model on multiple documents

# Step 1

Curate valid history data to feed to RAG model. 
Please head over to [openstax](https://openstax.org/) and download as many history realted text as you would like and store them in the data folder inside this project directory. The more data, the more context the RAG model covers.
More websites for history text data:
* [Center for Open Education](https://open.umn.edu/opentextbooks/subjects/history)
* [Gutenberg](https://www.gutenberg.org/ebooks/subject/58)


# Step 2

You will need to create an API key for Pinecone to use the vector embeddings database.
It is free to create, please head over to [Pinecone](https://www.pinecone.io/) and create an account then create a free API Key in the API Keys tab on the left
Once you have the key, please insert it in the RAG.py file where is says "YOUR API KEY HERE", leave the quotations.

# Step 3

Start Ollama if not running

# Step 4

On your terminal inside rag-history directory of this project start web application with:

    npm start

Go to your url running the web application on you machine, most often: [https://localhost:3000](https://localhost:3000)


# Step 5

Open RAG.py file inside src/Backend

__First Time Running Application__

If it is your first time either running **this** file (RAG.py)/following this option (**Option 1**), it is likely that you haven't vectorized the history data and stored it in the database. In order to do so make sure that any lines between where it says "If you are running for the first time / did not store embeddings in vector store" is uncommented.

Then make sure the lines between "If embeddings already stored in vector store" are commented

This is because the application is set to use the vector embeddings for sythesizing a response, and since it is your first time running the application, you will need to embed the data and store them in the vector store, so that future simulations won't need you to reembed all the data.

Lines that should be commented are 85-91


**Not First Time Running Application**

If it is **NOT** your first time either running **this** file (RAG.py)/following this option (**Option 1**), then it is likely that your data is embedded and store in your Pinecone vector database.

Then please to comment all the lines between "If you are running for the first time / did not store embeddings in vector store"

Then please uncomment the lines below "If embeddings already stored in vector store"


Run file:

    python3 RAG.py

or

Click play button


If done correctly you will see a chat engine on your web browser which you can ask questions. 
You can ask any question, however since the RAG model is for this option is trained only on the (Amendments of U.S.) data it will only provide
answers to questions related to the amendments of the U.S. Please give it time to respond as this is a free LLM model and can take up to 5 minutes,
to answer. In general only 1-2 minutes.

If you want the complete RAG model simulation for all history topics please see [Option 1](URL)
