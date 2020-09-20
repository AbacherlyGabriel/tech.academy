import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://yanhkawakami:<password>@pisi2020.qelym.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
print(db)