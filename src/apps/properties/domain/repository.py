from abc import ABC
from src.apps.properties.domain.models import CreateProperty, Property


class PropertiesRepositoryInterface(ABC):
    def get_all(self) -> Property:
        raise NotImplementedError

    def get_by_id(self, id: int) -> Property | None:
        raise NotImplementedError

    def filter_by_name(self, name: str) -> list[Property | None]:
        raise NotImplementedError

    def create_property(self, property_data: CreateProperty) -> list[Property]:
        raise NotImplementedError

    def delete_property(self, property_instance: Property) -> int:
        raise NotImplementedError


class PropertiesPaymentRepositoryInterface(ABC):
    def is_deletable(self, property_instance: Property) -> bool:
        raise NotImplementedError
