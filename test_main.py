from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_status():
    response = client.get("/")
    assert response.status_code == 200

def test_home_message():
    response = client.get("/")
    assert response.json() == {"mensagem": "API funcionando 🚀"}

def test_usuario_status():
    response = client.get("/usuario/1")
    assert response.status_code == 200

def test_usuario_id():
    response = client.get("/usuario/10")
    assert response.json()["usuario_id"] == 10

def test_usuario_tipo():
    response = client.get("/usuario/5")
    assert isinstance(response.json()["usuario_id"], int)