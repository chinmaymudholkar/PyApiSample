def test_create_post(client):
    # Arrange
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }

    # Act
    response = client.post("/posts", json=payload)

    # Assert
    assert response.status_code == 201
    data = response.json()

    assert data["id"] == 101  # JSONPlaceholder always returns 101 for new posts
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    # Clean up what we created
    client.delete(f"/posts/{data['id']}")
