from src.db.db import properties


class PropertiesRepository:
    db = properties

    def __new__(cls):
        """Creates a singleton"""
        if not hasattr(cls, "_instance"):
            cls._instance = super(PropertiesRepository, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_all(cls) -> list[dict]:
        return cls.db

    @classmethod
    def filter(cls, attribute: str, param: int | str) -> list[dict | None]:
        if isinstance(param, str):
            return list(filter(lambda prop: param in prop[attribute], cls.db))
        return list(filter(lambda prop: prop[attribute] == param, cls.db))

    @classmethod
    def create_property(cls, property_data: dict) -> list[dict]:
        cls.db.append(property_data)
        return cls.db

    @classmethod
    def update_property(cls, prop_obj: dict, property_data: dict) -> dict:
        prop_obj.update(property_data)
        return prop_obj
