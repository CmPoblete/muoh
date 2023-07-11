from src.apps.properties.application.service import PropertiesService


class TestServices:
    def test_create_property(self, dummy_repository, create_property_data_model):
        # setup
        service = PropertiesService(repository=dummy_repository)
        created_property_instance = service.create_property(
            property_data=create_property_data_model
        )
        assert created_property_instance.name == create_property_data_model.name
