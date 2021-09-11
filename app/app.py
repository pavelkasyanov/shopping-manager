from fastapi import FastAPI
from fastapi_jwt_auth.exceptions import AuthJWTException

from .api.auth import auth_router
from .api.auth.exception_handlers import authjwt_exception_handler
from .database import db


def get_app() -> FastAPI:
    application: FastAPI = FastAPI()

    db.init_app(application)

    application.add_exception_handler(
        AuthJWTException, authjwt_exception_handler
    )
    application.include_router(auth_router)

    return application


app = get_app()


@app.get("/ping")
async def index():
    return {"msg": "pong"}
