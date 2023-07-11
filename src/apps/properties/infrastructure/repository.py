from sqlalchemy.orm import Session

from src.db.sqlalchemy import engine
from src.apps.properties.domain.models import CreateProperty, Property
from src.apps.properties.infrastructure.orm_models import Property as ORMProperty
from src.apps.properties.domain.repository import PropertiesRepositoryInterface
from src.db.db import properties


# Mongo
class PropertiesRepository(PropertiesRepositoryInterface):
    db = properties

    def __new__(cls):
        """Creates a singleton"""
        if not hasattr(cls, "_instance"):
            cls._instance = super(PropertiesRepository, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_all(cls) -> list[Property]:
        return [Property(**prop) for prop in cls.db]

    @classmethod
    def filter(cls, attribute: str, param: int | str) -> list[Property | None]:
        if isinstance(param, str):
            properties = filter(lambda prop: param in prop[attribute], cls.db)
        else:
            properties = filter(lambda prop: prop[attribute] == param, cls.db)
        return [Property(**prop) for prop in properties if prop is not None]

    @classmethod
    def create_property(cls, property_data: CreateProperty) -> list[Property]:
        cls.db.append(property_data.dict())
        return [Property(**prop) for prop in cls.db]


# PostgreSQL


class PropertiesRepositorySQLAlchemy(PropertiesRepositoryInterface):
    @classmethod
    def get_all(cls) -> list[Property]:
        with Session(engine) as session:
            return [
                Property.from_orm(prop) for prop in session.query(ORMProperty).all()
            ]

    @classmethod
    def filter(cls, attribute: str, param: int | str) -> list[Property | None]:
        with Session(engine) as session:
            return [
                Property.from_orm(prop)
                for prop in session.query(ORMProperty)
                .filter(getattr(ORMProperty, attribute) == param)
                .all()
            ]

    @classmethod
    def create_property(self, property_data: CreateProperty) -> list[Property]:
        with Session(engine) as session:
            property_obj = ORMProperty(**property_data.dict())
            session.add(property_obj)
            session.commit()
            return Property.from_orm(property_obj)

    @classmethod
    def delete_property(self, property_instance: Property) -> int:
        with Session(engine) as session:
            property_obj = (
                session.query(ORMProperty)
                .filter(ORMProperty.id == property_instance.id)
                .first()
            )
            session.delete(property_obj)
            session.commit()
            return property_instance.id
