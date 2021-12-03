from fastapi.testclient import TestClient
from app.main import application


client = TestClient(application)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert 'Marcos' in response.json()[0]['first_name']
    assert 'Marvin' in response.json()[1]['first_name']
