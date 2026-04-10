def test_update_object(client, new_object):
    # Arrange
    payload = {
        "name": "Updated Test Device",
        "data": {"year": 2027, "price": 1099.99, "color": "Gold"},
    }

    # Act
    response = client.put(f"/objects/{new_object}", json=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == new_object
    assert data["name"] == "Updated Test Device"
    assert data["data"]["price"] == 1099.99
    assert data["data"]["color"] == "Gold"


def test_patch_object(client, new_object):
    # Arrange
    payload = {"name": "Patched Test Device"}

    # Act
    response = client.patch(f"/objects/{new_object}", json=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == new_object
    assert data["name"] == "Patched Test Device"
