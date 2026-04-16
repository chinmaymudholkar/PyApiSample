def test_update_post(client):
    # Arrange
    post_id = 1
    payload = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1,
    }

    # Act
    response = client.put(f"/posts/{post_id}", json=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == post_id
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"


def test_patch_post(client):
    # Arrange
    post_id = 1
    payload = {"title": "patched title"}

    # Act
    response = client.patch(f"/posts/{post_id}", json=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == post_id
    assert data["title"] == "patched title"
