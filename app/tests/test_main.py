from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

responseName = None

def test_call_name():
    global responseName
    responseName = client.get("/callname/Saran Kaewchuay")
    assert responseName.status_code == 200
    assert responseName.json() == {"hello": "Saran Kaewchuay"}
    
def test_post_name():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == responseName.json()
