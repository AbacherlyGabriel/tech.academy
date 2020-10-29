from flask import testing
from src.wsgi import app


def test_wsgi():
    with app.test_client() as test_client:
        response = test_client
        assert type(response) == testing.FlaskClient
