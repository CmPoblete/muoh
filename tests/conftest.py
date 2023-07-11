import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.apps.properties.domain.models import CreateProperty, Property
from src.apps.properties.domain.repository import PropertiesRepositoryInterface


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def create_property_data():
    return {"id": 1, "name": "Property 1", "image": "https://www.property1.com"}


@pytest.fixture
def create_property_data_model(create_property_data):
    return CreateProperty(
        name=create_property_data["name"], image=create_property_data["image"]
    )


@pytest.fixture
def dummy_repository():
    class DummyRepository(PropertiesRepositoryInterface):
        def create_property(self, property_data: CreateProperty) -> list[Property]:
            return Property(**property_data.dict(), id=1)

    return DummyRepository()
