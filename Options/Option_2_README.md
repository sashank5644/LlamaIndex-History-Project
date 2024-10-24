# Option 2

**Option 2**: Running the Retreival-Augmented Generation (RAG) model on 2 documents (Amendments of U.S)

# Step 1

Start Ollama if not already running

# Step 2

On your terminal inside rag-history directory of this project start web application with:

    npm start

Go to your url running the web application on you machine, most often: [https://localhost:3000](https://localhost:3000)


# Step 3

Open RAGTest.py file inside src/Backend and run file:

    python3 RAGTest.py

or

Click play button


If done correctly you will see a chat engine on your web browser which you can ask questions. 
You can ask any question, however since the RAG model is for this option is trained only on the (Amendments of U.S.) data it will only provide
answers to questions related to the amendments of the U.S. Please give it time to respond as this is a free LLM model and can take up to 5 minutes,
to answer. In general only 1-2 minutes.

If you want the complete RAG model simulation for all history topics please see [Option 1](Option_1_README.md)
