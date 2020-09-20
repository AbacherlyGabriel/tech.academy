from dao import UserDao

user_dao = UserDao()

def test_user_login():
    assert user_dao.read("admin", "pass") == True

def test_user_creation():
    assert user_dao.create("admin", "pass", "admin@admin.com") == False
