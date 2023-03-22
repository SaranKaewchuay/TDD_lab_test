from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
    
def test_hello():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World2"}


