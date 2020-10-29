from src.dao import UserDao


def test_dao_read():
    assert UserDao().read("admin@admin.com", "pass") is True


def test_dao_read_wrong_password():
    assert UserDao().read("admin@admin.com", "wrong") is False


def test_dao_create_error_different_passwords():
    assert UserDao().create("admin@admin.com", "admin", "pass", "wrong") is False


def test_dao_create_error_same_name():
    assert UserDao().create("admin@admin.com", "admin", "pass", "pass") is False


def test_dao_create_error_same_key():
    assert UserDao().create("admin@admin.com", "test", "pass", "pass") is False
