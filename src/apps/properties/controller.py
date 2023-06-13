from src.apps.properties.models import CreateProperty, Property
from src.apps.properties.repository import (
    PropertiesRepository,
    PropertiesRepositorySQLAlchemy,
)
from src.apps.properties.service import PropertiesService
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/properties")
def get_properties(
    name: str | None = None,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> list[Property]:
    if name:
        return service.filter_by_name(name=name)
    return service.get_all()


@router.get("/properties/{property_id}")
def get_properties_by_id(
    property_id: int,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> Property | None:
    return service.get_by_id(id=property_id)


@router.post("/properties")
def create_property(
    property_data: CreateProperty,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository(())),
    ),
) -> list[Property]:
    return service.create_property(property_data=property_data)
