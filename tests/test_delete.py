def test_delete_post(client):
    # Arrange
    post_id = 1

    # Act
    response = client.delete(f"/posts/{post_id}")

    # Assert
    assert response.status_code == 200
    # JSONPlaceholder returns an empty object on successful delete
    assert response.json() == {}
