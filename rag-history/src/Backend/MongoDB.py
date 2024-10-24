from pymongo import MongoClient
from datetime import datetime

cluster = "Your MongoDB Driver Connection"
client = MongoClient(cluster)

db = client.RAG
chat_history = db["User Data"]

def store_chat_message(user_id, question, response):
    chat_data = {
        "user_id": user_id,
        "question": question,
        "response": response,
        "timestamp": datetime.now()
    }
    chat_history.insert_one(chat_data)

def get_chat_history(user_id):
    chat = chat_history.find({"user_id": user_id})
    ls = []
    for data in chat:
        ls.append({
            "id": str(data["_id"]),  # Convert ObjectId to string
            "question": "Question: " + str(data["question"]),
            "response": "Response: " + str(data["response"]),
            "timestamp": str(data["timestamp"]) if "timestamp" in data else "",
            "user_id": data["user_id"]
        })
    return ls

from bson import ObjectId
def delete_chat_message(message_id, user_id):
    try:
        result = chat_history.delete_one({
            "_id": ObjectId(message_id),
            "user_id": user_id 
        })
        return result.deleted_count > 0
    except Exception as e:
        print(f"Error deleting message: {e}")
        return False
    