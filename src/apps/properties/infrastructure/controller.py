from src.apps.properties.domain.models import CreateProperty, Property
from src.apps.properties.infrastructure.repository import (
    PropertiesRepositorySQLAlchemy,
)
from src.apps.properties.infrastructure.integrations.payments import (
    PropertyPaymentsIntegration,
)
from src.apps.properties.application.service import PropertiesService
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/properties")
def get_properties(
    name: str | None = None,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepositorySQLAlchemy())
    ),
) -> list[Property]:
    if name:
        return service.filter_by_name(name=name)
    return service.get_all()


@router.get("/properties/{property_id}")
def get_properties_by_id(
    property_id: int,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepositorySQLAlchemy())
    ),
) -> Property:
    return service.get_by_id(id=property_id)


@router.post("/properties")
def create_property(
    property_data: CreateProperty,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepositorySQLAlchemy()),
    ),
) -> Property:
    return service.create_property(property_data=property_data)


@router.delete("/properties/{property_id}")
def delete_property(
    property_id: int,
    service: PropertiesService = Depends(
        lambda: PropertiesService(
            repository=PropertiesRepositorySQLAlchemy(),
            property_payment_repository=PropertyPaymentsIntegration(),
        )
    ),
) -> dict:
    return {"id": service.delete_property(property_id=property_id)}
