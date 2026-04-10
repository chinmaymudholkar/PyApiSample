def test_get_all_objects(client):
    # Arrange: No specific setup required for fetching all objects.

    # Act
    response = client.get("/objects")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]


def test_get_single_object(client, new_object):
    # Arrange: `new_object` fixture handles object creation implicitly.

    # Act
    response = client.get(f"/objects/{new_object}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_object
    assert data["name"] == "Test Device"
    assert data["data"]["price"] == 999.99
