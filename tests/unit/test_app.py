from src.app import app


def test_home_page():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"tech.academy | home" in response.data


def test_register_page():
    with app.test_client() as test_client:
        response = test_client.get('/register')
        assert response.status_code == 200
        assert b"tech.academy | sign up" in response.data


def test_login_page():
    with app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        assert b"tech.academy | login" in response.data


def test_about_page():
    with app.test_client() as test_client:
        response = test_client.get('/about')
        assert response.status_code == 200
        assert b"tech.academy | about" in response.data


def test_profile_page():
    with app.test_client() as test_client:
        response = test_client.get('/perfil')
        assert response.status_code == 200
        assert b"ech.academy | meu perfil" in response.data


def test_page_not_found():
    with app.test_client() as test_client:
        response = test_client.get('/notexist')
        assert response.status_code == 404