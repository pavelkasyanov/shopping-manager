import logging

from fastapi import APIRouter, Depends, Request, Response
from fastapi_jwt_auth import AuthJWT
from app.templates import templates

views_router = APIRouter()

logger = logging.getLogger(__file__)


@views_router.get("/")
@views_router.get("/signin")
async def index(request: Request) -> Response:
    return templates.TemplateResponse(
        "index.html", context={"request": request}
    )


@views_router.get("/home")
async def home(request: Request, Authorize: AuthJWT = Depends()) -> Response:

    Authorize.jwt_required()

    return templates.TemplateResponse(
        "index.html", context={"request": request}
    )
