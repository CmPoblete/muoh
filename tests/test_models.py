from src.apps.properties.domain.models import Property


class TestModels:
    def test_property_instance(self, create_property_data):
        property_instance = Property(**create_property_data)
        assert property_instance.name == create_property_data["name"]
        assert property_instance.image == create_property_data["image"]
