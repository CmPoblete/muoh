from random import choices
from src.apps.properties.domain.models import Property
from src.apps.properties.domain.repository import PropertiesPaymentRepositoryInterface

possible_responses = [
    {"status": 200, "content": "True"},
    {"status": 400, "content": "Bad Request"},
    {"status": 500, "content": "Internal Server Error"},
    {"status": 504, "content": "Gateway Timeout"},
]


class GenericPaymentIntegrationException(Exception):
    ...


class PropertyPaymentsIntegration(PropertiesPaymentRepositoryInterface):
    def __init__(self, silent_exceptions: bool = False) -> None:
        self.silent_exceptions = silent_exceptions

    def get_response(self, property_instance: Property) -> dict:
        response = choices(possible_responses, weights=[100, 0, 0, 0])[0]
        if self.silent_exceptions:
            return response
        if response["status"] != 504:  # Timeout
            # Retry request
            raise GenericPaymentIntegrationException
        if response["status"] != 200:
            raise GenericPaymentIntegrationException
        return response

    def is_deletable(self, property_instance: Property) -> bool:
        response = choices(possible_responses, weights=[100, 0, 0, 0])[0]
        return response["content"] == "True"
