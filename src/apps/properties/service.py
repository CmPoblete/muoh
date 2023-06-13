from src.apps.properties.models import CreateProperty, Property
from src.apps.properties.repository import PropertiesRepository


class PropertiesService:
    def __init__(self, repository: PropertiesRepository) -> None:
        self.repository = repository

    def get_all(self) -> Property:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Property | None:
        property_query = self.repository.filter(attribute="id", param=id)
        if property_query:
            return property_query[0]
        return None

    def filter_by_name(self, name: str) -> list[Property | None]:
        return self.repository.filter(attribute="name", param=name)

    def create_property(self, property_data: CreateProperty) -> list[Property]:
        return self.repository.create_property(property_data=property_data)
