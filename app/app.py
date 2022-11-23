from fastapi import FastAPI
from fastapi_jwt_auth.exceptions import AuthJWTException
from sqlalchemy_utils import database_exists, create_database

from settings import settings
from .api.auth import auth_router
from .api import v1 as v1_api
from .api.auth.exception_handlers import authjwt_exception_handler
from app.infrastructure.database.db import db


def get_app() -> FastAPI:
    application: FastAPI = FastAPI()

    application.add_exception_handler(
        AuthJWTException, authjwt_exception_handler
    )

    application.include_router(auth_router)
    application.include_router(v1_api.api_router)

    return application


app = get_app()


@app.on_event("startup")
async def startup_event():
    if not database_exists(settings.DB_DSN):
        create_database(settings.DB_DSN)
    db.init_app(app)


@app.get("/ping")
async def index():
    return {"msg": "pong"}
