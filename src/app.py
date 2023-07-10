from fastapi import FastAPI

from src.apps.properties.infrastructure.controller import router as PropertiesRouter
from src.apps.properties.infrastructure.error_handlers import (
    property_not_found_exception_handler,
    property_not_deletable_exception_handler,
)
from src.apps.properties.domain.exceptions import (
    PropertyNotFoundException,
    PropertyNotDeletableException,
)

app = FastAPI()
app.include_router(PropertiesRouter)
app.add_exception_handler(
    PropertyNotFoundException, property_not_found_exception_handler
)
app.add_exception_handler(
    PropertyNotDeletableException,
    property_not_deletable_exception_handler,
)


@app.get("/")
def hellow_world():
    return {"data": "hellow world"}
