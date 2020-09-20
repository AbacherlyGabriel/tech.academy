import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://yanhkawakami:<password>@pisi2020.qelym.mongodb.net/")
db = client.database.collection
print(db)