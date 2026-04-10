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
    """Fixture to create a new object and yield its ID, deleting it after test."""
    payload = {
        "name": "Test Device",
        "data": {"year": 2026, "price": 999.99, "color": "Silver"},
    }
    response = client.post("/objects", json=payload)
    data = response.json()
    obj_id = data["id"]

    yield obj_id

    # Teardown
    client.delete(f"/objects/{obj_id}")
