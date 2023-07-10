from src.apps.properties.domain.models import CreateProperty, Property
from src.apps.properties.domain.repository import (
    PropertiesRepositoryInterface,
    PropertiesPaymentRepositoryInterface,
)
from src.apps.properties.domain.exceptions import (
    PropertyNotFoundException,
    PropertyNotDeletableException,
)


class PropertiesService:
    def __init__(
        self,
        repository: PropertiesRepositoryInterface,
        property_payment_repository: PropertiesPaymentRepositoryInterface = None,
    ) -> None:
        self.repository = repository
        self.property_payment_repository = property_payment_repository

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

    def delete_property(self, property_id: int) -> int:
        property_instance = self.get_by_id(id=property_id)
        if not property_instance:
            raise PropertyNotFoundException(property_id=property_id)
        property_deletable = self.property_payment_repository.is_deletable(
            property_instance=property_instance
        )
        if not property_deletable:
            raise PropertyNotDeletableException(property_id=property_id)
        return self.repository.delete_property(property_instance=property_instance)
