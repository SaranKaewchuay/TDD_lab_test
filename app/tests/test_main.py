from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

Name = None

def test_call_name():
    response = client.get("/callname/Saran Kaewchuay")
    global Name
    Name = "Saran Kaewchuay"
    assert response.status_code == 200
    assert response.json() == {"hello": "Saran Kaewchuay"}
    
def test_post_name():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == {"hello": Name}
