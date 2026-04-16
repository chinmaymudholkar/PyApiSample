def test_get_all_posts(client):
    # Arrange: No specific setup required for fetching all posts.

    # Act
    response = client.get("/posts")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]


def test_get_single_post(client):
    # Arrange: Use a known existing post ID (e.g., 1) because JSONPlaceholder
    # is a mock API that doesn't persist created resources.
    post_id = 1

    # Act
    response = client.get(f"/posts/{post_id}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data
    assert "body" in data
