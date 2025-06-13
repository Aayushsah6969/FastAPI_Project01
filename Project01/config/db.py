from pymongo import MongoClient


MONGO_URI="<your db url here>"

conn = MongoClient(MONGO_URI)
