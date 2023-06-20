from pymongo.mongo_client import MongoClient

MONGO_URL = "mongodb://mongodb:27017/"

client = MongoClient(MONGO_URL)
muoh_db = client["muoh"]
if muoh_db["properties"] is None:
    muoh_db.create_collection("properties")
