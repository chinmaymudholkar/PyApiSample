def test_delete_object(client, new_object):
    # Arrange: `new_object` fixture handles object creation implicitly.

    # Act
    response = client.delete(f"/objects/{new_object}")

    # Assert
    assert response.status_code == 200
    data = response.json()

    # The API returns {"message": "Object with id = x has been deleted."}
    assert "deleted" in data.get("message", "").lower()

    # Verify it's actually deleted
    get_response = client.get(f"/objects/{new_object}")
    assert get_response.status_code == 404
