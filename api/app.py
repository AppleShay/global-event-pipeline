from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["event_db"]
collection = db["events"]

@app.get("/")
def root():
    return {"message": "Global Event Pipeline API is running!"}

@app.get("/events")
def get_events():
    events = list(collection.find({}, {"_id": 0}))
    return {"events": events}
