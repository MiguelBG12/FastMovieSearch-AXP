from fastapi.testclient import TestClient
from app.api.profile import router
from app.schemas.profile import ProfileCreate

client = TestClient(router)

def test_create_profile():
    """
    Test creating a profile using the /profiles/ endpoint.
    """
    profile_data = {"id": 1, "name": "John Doe", "description": "A test profile"}
    response = client.post("/profiles/", json=profile_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["description"] == "A test profile"


def test_get_profile():
    """
    Test retrieving a profile by its ID using the /profiles/{profile_id} endpoint.
    """
    response = client.get("/profiles/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["description"] == "A test profile"
