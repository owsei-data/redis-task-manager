from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI") #variavel local railway

#settings
db = client('task-manager') #set db
colecao = db['user']