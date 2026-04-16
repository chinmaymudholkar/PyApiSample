def test_get_non_existent_post(client):
    # Act
    response = client.get("/posts/9999")

    # Assert
    assert response.status_code == 404
    assert response.json() == {}


def test_create_post_invalid_payload(client):
    # Act
    # JSONPlaceholder is very permissive, it might even accept invalid payloads
    # and just return the payload back with an ID.
    response = client.post("/posts", json={"invalid": "data"})

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    # Cleanup
    client.delete(f"/posts/{data['id']}")
