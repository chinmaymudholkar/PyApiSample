def test_create_object(client):
    # Arrange
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        },
    }

    # Act
    response = client.post("/objects", json=payload)

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["data"]["year"] == 2019

    # Clean up what we created
    client.delete(f"/objects/{data['id']}")
