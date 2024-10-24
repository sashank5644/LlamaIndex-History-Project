# History Agent (RAG)

# UI
<img width="1287" alt="Screen Shot 2024-10-12 at 10 28 14 PM" src="https://github.com/user-attachments/assets/6a0f0e3d-0309-4891-923f-6968be9949a5">
<img width="1290" alt="Screen Shot 2024-10-12 at 10 28 59 PM" src="https://github.com/user-attachments/assets/ffb76e19-c1ef-470e-ac1e-6d1e836902e2">
<img width="1287" alt="Screen Shot 2024-10-12 at 10 29 51 PM" src="https://github.com/user-attachments/assets/eefc5c9d-2d14-4ed2-8b5b-793f3b7ff34e">

# Project Overview

The History Agent project is a full-stack web application designed as an expert chat engine for historical inquiries. Leveraging the principles of Retrieval-Augmented Generation (RAG), this application utilizes the advanced Llama 3 language model to deliver evidence-based responses to historical questions.

Built on the FRAP stack (Flask, React, API, Pinecone), the project harnesses the following technologies:

* Flask: Serves as the backend framework, providing robust integration capabilities and handling API requests efficiently.
* React: Provides robust framework for the frontend user interface, delivering a responsive and engaging experience for users.
* API: Facilitates seamless communication between the frontend and backend components of the application.
* Pinecone: Manages the database, enabling efficient storage and retrieval of embeddings for enhanced query responses.

# Purpose
This comprehensive architecture ensures that the History Agent delivers accurate and contextually relevant answers, positioning it as a valuable resource for history enthusiasts, researchers, and students alike. By leveraging the capabilities of the Llama 3 language model and Retrieval-Augmented Generation, the application not only provides reliable information but also serves as an effective and efficient learning tool. It enhances users' understanding of historical concepts and events, fostering a more streamlined learning experience.


# Project Functionalities

1. **Historical Question-Answering**: Provides accurate, evidence-based answers to historical inquiries using the Llama 3 language model and Retrieval-Augmented Generation (RAG).
2. **User-Friendly Interface**: Features an intuitive and engaging frontend built with React, ensuring ease of use and real-time interaction.
3. **Optimized Model Performance**: Trained with the most efficient hyperparameters to deliver the most accurate possible answers, enhancing the overall learning experience.
4. **Efficient Learning Tool**: Supports students and researchers by facilitating efficient study habits and deeper engagement with historical content.
5. **Seamless Integration**: Utilizes CORS for smooth interaction between frontend and backend, built on the scalable FRAP stack (Flask, React, API, Pinecone).
6. **Data Management**: Utilizes Pinecone for efficient storage and retrieval of vector embeddings, enhancing query performance.



# Repository Structure

* Options: Instructions for running option 1 and option 2 (SEE BELOW FOR MORE INFO)
* Test Data: Comprises of 2 documents (Amendments of U.S.) and is used for quick testing without pinecone account creation (READ BELOW FOR MORE INFORMATION)
* Data: Includes initial 2 documents (Amendments of U.S.) and will be used to store openly available history text data
* rag-history: Contains React application with CSS components, and stores Flask framework with Python, integrated with Pinecone.


# Getting Started

There are 2 simulations offered for this project:

Select one of the options for testing the project, and follow the instructions after for intial setup as they are required for either option.

[Option 1](Options/Option_1_README.md). Run complete RAG application for history

   * (Longer runtime, application performs the functionalties for History Agent)
   * Uses vector database and requires Pinecone account creation for API key
   * You will need to download free history text data from available websites

[Option 2](Options/Option_2_README.md). Run test RAG application using only 2 documents (Amendments of U.S.) as data
    
   * (Faster, used for quick testing of application and doesn't require Pinecone account creation)
   * Application can answer questions about U.S. Amendments)
   * No need to download external history text data


**Initial Setup**

To run this full stack project, you will need to run both the frontend and backend portions of the application. Each respective part and their detailed instructions for setup, configurations, and deployment are described below.

For this project you will need **Python version 3.11.10**

You will also need **Ollama** to run the local LLM model

Download https://ollama.com/

It is best to create a virtual environment to manage the required dependencies and framework versions for this project. To initialize and set up a virtual environment, first clone this repository to your local development environment.

    git clone <repository-url>

**Create a Virtual Environmet**

    python3 -m venv venv


**Activate the Virtual Environment**

* MacOS/Linux:

      source venv/bin/activate

* Windows:

      venv\Scripts\activate

**Install Dependencies (backend)**

      pip install -r requirements.txt

**Navigate to rag-history directory**

      cd rag-history

**Install Node Modules, Axios, and Fontawesome if Not Already Installed (Frontend)**

      npm install @fortawesome/react-fontawesome @fortawesome/free-solid-svg-icons

      
Please follow the above instructions and select an option ([Option 1](Options/Option_1_README.md)) or ([Option 2](Options/Option_2_README.md)) to simulate the application on your local deployment environemnt.

