from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

from app.domain.deps import Services
from app.domain.services.authentication_service import AuthenticationService


async def get_authentication_service() -> AuthenticationService:
    return Services.authentication_service
