from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local
collection = db.mongo_start

collection.insert_one({
    "title": "Mongo Start!",
    "Content": "by FastCampus Course"
})

rows = collection.find()

for row in rows:
    print(row)
    
    
row = collection.find_one({'title': "Mongo Start!"})
print(row)