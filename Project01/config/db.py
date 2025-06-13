from pymongo import MongoClient


MONGO_URI="mongodb+srv://aayushsah269:0RbjxUrprp3T342S@cluster0.it7to2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0/AllNotes"

conn = MongoClient(MONGO_URI)