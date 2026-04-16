import pytest

from core.api_client import ApiClient


@pytest.fixture(scope="session")
def client():
    """Provide a session-scoped API client instance."""
    api_client = ApiClient()
    yield api_client
    api_client.close()


@pytest.fixture
def new_object(client):
    """Fixture to create a new post and yield its ID, deleting it after test."""
    payload = {
        "title": "Test Post",
        "body": "This is a test post.",
        "userId": 1,
    }
    response = client.post("/posts", json=payload)
    data = response.json()
    obj_id = data["id"]

    yield obj_id

    # Teardown
    client.delete(f"/posts/{obj_id}")
