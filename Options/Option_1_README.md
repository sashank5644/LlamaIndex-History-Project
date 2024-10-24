# Option 1

**Option 1**: Running the Retreival-Augmented Generation (RAG) model on multiple documents

# Step 1

Curate valid history data to feed to RAG model. 
Please head over to [free history textbook website](https://glhssocialstudies.weebly.com/world-history-textbook---pdf-copy.html) and download as many history realted pdf files from "World History" and "U.S. History" as you would like and store them in the "data" folder inside this project directory. The more data, the more context the RAG model covers.

More websites for history text data:
* [OpenStax](https://openstax.org/)
* [Center for Open Education](https://open.umn.edu/opentextbooks/subjects/history)
* [Gutenberg](https://www.gutenberg.org/ebooks/subject/58)


# Step 2

You will need to create an API key for Pinecone to use the vector embeddings database.
It is free to create, please head over to [Pinecone](https://www.pinecone.io/) and create an account then create a free API Key in the API Keys tab on the left
Once you have the key, please insert it in the RAG.py file where is says "YOUR API KEY HERE", leave the quotations.

# Step 3

You need to create a MongoDB account for managing previous history chat information.
It is free to create, please head over to [MongoDB](https://www.mongodb.com/) and create an account.
Next, navigate to the ATLAS cloud platform and create a new Project with default settings
Navigate to your newly created project and build a new cluster on AWS cloud services and your region
Create a databse inside the cluster, name it "RAG", and name the collection "User Data"
Connect using native connection, make sure to select python and most recent version of Mongo driver
Make sure to insert your unique driver connection link in MongoDB.py where it says "Your MongoDB Driver Connection" 

# Step 4

Start Ollama if not already running

# Step 5

On your terminal inside rag-history directory of this project start web application with:

    npm start

Go to your url running the web application on you machine, most often: [https://localhost:3000](https://localhost:3000)


# Step 6

Open RAG.py file inside src/Backend

**First Time Running Application**

If it is your first time either running **this** file (RAG.py)/following this option (**Option 1**), it is likely that you haven't embedded the history data and stored it in the database. In order to do so make sure that any lines between where it says "If you are running for the first time / did not store embeddings in vector store" is **uncommented**.

Then make sure the lines between "If embeddings already stored in vector store" are **commented**

Lines that should be commented are 85-91

This is because the application is set to use the vector embeddings for sythesizing a response, and since it is your first time running the application, you will need to embed the data and store them in the vector store, so that future simulations won't need you to embed all the data again.

Please be patient, as depending on the amount of data fed, the embedding process can vary in time, generally running this for the first time takes a while because of the content and resources it is working with. If you want to test it quicker please see ([Option 2](Option_2_README.md)).


**Not First Time Running Application**

If it is **NOT** your first time either running **this** file (RAG.py)/following this option (**Option 1**), then it is likely that your data is embedded and store in your Pinecone vector database.

Then please to **comment all** the lines between "If you are running for the first time / did not store embeddings in vector store"

Then please **uncomment** the lines below "If embeddings already stored in vector store"


Run file:

    python3 RAG.py

or

Click play button


If done correctly you will see a chat engine on your web browser where you can ask questions. 
You can ask any question, and depending on the amount of history text data you have fed into the RAG model, it will provide
answers to questions related to what is present in the data you fed. Please give it time to respond as this is a free LLM model and can take up to 5 minutes
to answer. 

If you want the quicker RAG model simulation for testing the application on smaller data please see [Option 2](Option_2_README.md).
