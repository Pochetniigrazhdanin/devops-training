from app.main import app

client = app.test_client()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_main():
    response = client.get("/")
    assert response.status_code == 200

def test_health_returns_json():
    response = client.get("/health")

    data = response.get_json()

    assert data is not None
    assert data["status"] == "ok"