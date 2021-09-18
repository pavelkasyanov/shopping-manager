from fastapi import Depends, HTTPException

from fastapi_jwt_auth import AuthJWT

from app.domain.deps import Services
from app.domain.models.auth_user_claims import AuthUserClaims
from app.domain.services.users_service import UserService


def get_user_service() -> UserService:
    return Services.user_service


async def get_authorized_user(authorize: AuthJWT = Depends()) -> AuthUserClaims:
    authorize.jwt_required()
    return AuthUserClaims(**authorize.get_raw_jwt())


async def get_authorized_superuser(
    auth_user_claims: AuthUserClaims = Depends(get_authorized_user),
) -> AuthUserClaims:
    if not auth_user_claims.is_superuser:
        raise HTTPException(403)
    return auth_user_claims
