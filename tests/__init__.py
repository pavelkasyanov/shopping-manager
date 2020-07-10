import json

import pytest

from src.http.app import create_app


class AuthData:
    access_token = None
    refresh_token = None

    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


@pytest.yield_fixture(scope='module')
def test_client():
    flask_app = create_app('postgresql://postgres:postgres@localhost:5432/shopping_manager?client_encoding=utf8',
                           testing=True)
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def login(client):
    response = client.post("/security/login",
                           data=json.dumps({"login": "admin",
                                            "password": "password"}),
                           content_type='application/json')
    assert response.status_code == 200

    json_data = response.json

    if not json_data['login']:
        raise Exception("Invalid login or password")

    return AuthData(response.json['access_token'], response.json['refresh_token'])