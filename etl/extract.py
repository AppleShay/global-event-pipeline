import os
import requests
import yaml
from pymongo import MongoClient

# Load config
with open("/app/config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["newsapi_key"]
API_URL = config["newsapi_url"]
COUNTRY = config["country"]

# Mongo connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URI)
db = client["event_db"]
collection = db["events"]

def run_etl():
    print("📡 Fetching news from NewsAPI...")
    params = {
        "country": COUNTRY,
        "apiKey": API_KEY,
        "pageSize": 5
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if response.status_code != 200 or "articles" not in data:
        print(f"❌ Failed to fetch news: {data}")
        return

    # Transform: store only required fields
    events = []
    for article in data["articles"]:
        events.append({
            "title": article["title"],
            "description": article.get("description"),
            "source": article["source"]["name"],
            "url": article["url"],
            "publishedAt": article["publishedAt"]
        })

    # Load into Mongo
    collection.delete_many({})
    collection.insert_many(events)
    print(f"✅ Inserted {len(events)} events into MongoDB")

if __name__ == "__main__":
    run_etl()
