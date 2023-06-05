from src.apps.properties.repository import PropertiesRepository


class PropertiesService:
    def __init__(self, repository: PropertiesRepository) -> None:
        self.repository = repository

    def get_all(self) -> dict:
        return self.repository.get_all()

    def get_by_id(self, id: int) -> dict | None:
        property_query = self.repository.filter(attribute="id", param=id)
        if property_query:
            return property_query[0]
        return None

    def filter_by_name(self, name: str) -> list[dict | None]:
        return self.repository.filter(attribute="name", param=name)

    def create_property(self, property_data: dict) -> list[dict]:
        return self.repository.create_property(property_data=property_data)

    def update_property_by_id(self, id: int, property_data: dict) -> dict:
        filter_prop = self.repository.filter(attribute="id", param=id)
        if filter_prop:
            return self.repository.update_property(
                prop_obj=filter_prop[0], property_data=property_data
            )
        return None
