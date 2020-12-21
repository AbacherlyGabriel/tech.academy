import os

from pymongo import errors, MongoClient

db_pass = os.environ.get('DBPASS')
client = MongoClient(
    f"mongodb+srv://yanhkawakami:{db_pass}@pisi2020.qelym.mongodb.net/")


class UserDao:

    def __init__(self):
        self.users_db = client['users']
        self.login_col = self.users_db['login']
        self.message = ''
        self.cursos_db = client['cursos']
        self.teste_col = self.cursos_db['teste']

    def read(self, email, password):
        query = {"_id": email, "pass": password}
        doc = self.login_col.find_one(query)
        if (doc is not None):
            self.nome = doc['user']
            return True
        return False

    def create_user(self, email, user, password, valida_password):
        try:
            if (password != valida_password):
                self.message = "As senhas não coincidem"
                return False
            query = {"user": user}
            doc = self.login_col.find_one(query)
            if (doc is not None):
                self.message = "Nome de usuário em uso"
                return False
            doc = {"_id": email, "user": user, "pass": password}
            self.login_col.insert_one(doc)
            return True
        except errors.DuplicateKeyError:
            self.message = "Email já cadastrado"
            return False


class SearchDao:

    def query_by_description(self, description):
        query = {"descricao": {"$regex": f"{description}", "$options": 'i'}}
        docs = self.teste_col.find(query)
        return docs
