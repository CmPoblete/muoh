class PropertyNotFoundException(Exception):
    def __init__(self, property_id: int) -> None:
        self.property_id = property_id


class PropertyNotDeletableException(Exception):
    def __init__(self, property_id: int) -> None:
        self.property_id = property_id
