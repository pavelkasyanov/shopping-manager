def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}


def test_404(client):
    response = client.get("/test-url")
    assert response.status_code == 404
