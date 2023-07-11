from src.apps.properties.infrastructure.repository import PropertiesRepositorySQLAlchemy


class TestRepositories:
    def test_get_all(self):
        # setup
        properties = PropertiesRepositorySQLAlchemy.get_all()
        assert len(properties) > 0

    def test_create_property(self, create_property_data_model):
        property_instance = PropertiesRepositorySQLAlchemy.create_property(
            property_data=create_property_data_model
        )
        assert property_instance.name == create_property_data_model.name
