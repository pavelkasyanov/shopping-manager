from fastapi import FastAPI
from fastapi_jwt_auth.exceptions import AuthJWTException

from .api.auth import auth_router
from .api.auth.exception_handlers import authjwt_exception_handler

app = FastAPI()


app.add_exception_handler(AuthJWTException, authjwt_exception_handler)

app.include_router(auth_router)


@app.get("/ping")
async def index():
    return {"msg": "pong"}
