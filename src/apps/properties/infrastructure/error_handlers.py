from fastapi import status, Request
from fastapi.responses import JSONResponse
from src.apps.properties.domain.exceptions import (
    PropertyNotFoundException,
    PropertyNotDeletableException,
)
import logging

logger = logging.getLogger(__name__)


def handle_exception_response(
    request: Request, exc: Exception, status_code: status, content: dict
) -> JSONResponse:
    logger.error(
        f"Exception occurred in URL {request.url}: {exc.__class__.__name__}: {content}"
    )
    return JSONResponse(
        status_code=status_code,
        content=content,
    )


async def property_not_found_exception_handler(
    request: Request, exc: PropertyNotFoundException
):
    return handle_exception_response(
        request=request,
        exc=exc,
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Oops! Property id {exc.property_id} not found!"},
    )


async def property_not_deletable_exception_handler(
    request: Request, exc: PropertyNotDeletableException
):
    return handle_exception_response(
        request=request,
        exc=exc,
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"Oops! Property id {exc.property_id} not deletable!"},
    )
