from src.dao import UserDao

def test_dao_read():
    assert UserDao().read("admin@admin.com", "pass") is True


def test_dao_create():
    assert UserDao().create("admin@admin.com", "admin", "pass", "pass") is False
