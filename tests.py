from src.dao import UserDao

def test_dao_read():
    assert UserDao().read("admin@admin.com", "pass") == True