
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://chaturvedihimanshu120_db_user:iCF9jmvl3UE4FNpj@ac-uojyw7r-shard-00-00.zg5lfqe.mongodb.net:27017,ac-uojyw7r-shard-00-01.zg5lfqe.mongodb.net:27017,ac-uojyw7r-shard-00-02.zg5lfqe.mongodb.net:27017/?ssl=true&replicaSet=atlas-k4f90k-shard-0&authSource=admin&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)