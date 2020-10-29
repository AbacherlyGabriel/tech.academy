from src.app import app


def test_home_page():
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_register_page():
    with app.test_client() as test_client:
        response = test_client.get('/register')
        assert response.status_code == 200


def test_login_page():
    with app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200


def test_about_page():
    with app.test_client() as test_client:
        response = test_client.get('/about')
        assert response.status_code == 200


def test_profile_page():
    with app.test_client() as test_client:
        response = test_client.get('/perfil')
        assert response.status_code == 200


def test_page_not_found():
    with app.test_client() as test_client:
        response = test_client.get('/notexist')
        assert response.status_code == 404
