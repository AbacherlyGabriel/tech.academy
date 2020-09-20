from pymongo import errors, MongoClient

client = MongoClient(
    "mongodb+srv://yanhkawakami:<password>@pisi2020.qelym.mongodb.net/")


class UserDao:

    def __init__(self):
        self.db = client['users']
        self.col = self.db['login']

    def read(self, user, password):
        query = {"_id": user, "pass": password}
        doc = self.col.find_one(query)
        if (doc != None):
            return True
        return False

    def create(self, user, email, password):
        try:
            doc = {"_id": user, "email": email, "pass": password}
            aux = self.col.insert_one(doc)
            return True
        except errors.DuplicateKeyError as err:
            return False