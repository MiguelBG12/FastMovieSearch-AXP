from fastapi.testclient import TestClient
from app.api.user import router
from app.schemas.user import UserCreate

client = TestClient(router)

def test_create_user():
    """
    Test creating a user using the /users/ endpoint.
    """
    user_data = {"email": "test@example.com", "profiles": []}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_user():
    """
    Test retrieving a list of users using the /users/ endpoint.
    """
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json()[0]["email"] == "test@example.com"
