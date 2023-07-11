class TestAPI:
    def test_get(self, client):
        response = client.get("/")
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["data"] == "hellow world"

    def test_get_non_existent_property(self, client):
        response = client.get("/properties/425125")
        assert response.status_code == 404

    def test_create_and_retrieve(self, client, create_property_data_model):
        response = client.post("/properties", json=create_property_data_model.dict())
        response_json = response.json()
        assert response.status_code == 200
        created_property_id = response_json["id"]
        response = client.get(f"/properties/{created_property_id}")
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["name"] == create_property_data_model.name
        assert response_json["image"] == create_property_data_model.image
