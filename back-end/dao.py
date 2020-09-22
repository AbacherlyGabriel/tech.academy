import os

from pymongo import errors, MongoClient

db_pass = os.environ.get('DBPASS')
client = MongoClient(
    f"mongodb+srv://yanhkawakami:{db_pass}@pisi2020.qelym.mongodb.net/")


class UserDao:

    def __init__(self):
        self.db = client['users']
        self.col = self.db['login']

    def read(self, email, password):
        query = {"_id": email, "pass": password}
        doc = self.col.find_one(query)
        if (doc != None):
            self.nome = doc['user']
            return True
        return False

    def create(self, email, user, password):
        try:
            doc = {"_id": email, "user": user, "pass": password}
            aux = self.col.insert_one(doc)
            return True
        except errors.DuplicateKeyError as err:
            return False
