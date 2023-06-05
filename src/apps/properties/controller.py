from typing import Any
from src.apps.properties.repository import PropertiesRepository
from src.apps.properties.service import PropertiesService
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/properties")
def get_properties(
    name: str | None = None,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> list[dict]:
    if name:
        return service.filter_by_name(name=name)
    return service.get_all()


@router.get("/properties/{property_id}")
def get_properties_by_id(
    property_id: int,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> dict | None:
    return service.get_by_id(id=property_id)


@router.post("/properties")
def create_property(
    property_data: dict,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> list[dict]:
    return service.create_property(property_data=property_data)


@router.patch("/properties/{property_id}")
def update_property(
    property_id: int,
    property_data: dict,
    service: PropertiesService = Depends(
        lambda: PropertiesService(repository=PropertiesRepository())
    ),
) -> dict:
    return service.update_property_by_id(id=property_id, property_data=property_data)
