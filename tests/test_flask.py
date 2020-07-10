import json

from tests import login, test_client

from version import __app_version__ as app_version


def test_login(test_client):
    response = test_client.post("/security/login",
                                data=json.dumps({"login": "admin",
                                                 "password": "password"}),
                                content_type='application/json')
    assert response.status_code == 200


def test_app_version(test_client):
    auth_data = login(test_client)

    response = test_client.get('/api/version',
                               headers={'Authorization': 'Bearer {}'.format(auth_data.access_token)})

    assert response.status_code == 200
    assert app_version in response.json
