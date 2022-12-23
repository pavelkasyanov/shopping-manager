import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT

from app.domain.types import NotFoundError, VerificationFailError
from settings import settings

from ...domain.models.auth_user_claims import AuthUserClaims
from ...domain.services.authentication_service import AuthenticationService
from .depends import get_authentication_service
from .models import AuthUser

auth_router = APIRouter()

logger = logging.getLogger(__file__)


@auth_router.post("/login")
async def login(
    auth_user: AuthUser,
    authorize: AuthJWT = Depends(),
    authentication_service: AuthenticationService = Depends(
        get_authentication_service
    ),
) -> JSONResponse:
    try:
        current_user = await authentication_service.verify_user(
            auth_user.username, auth_user.password
        )
        if not current_user:
            raise Exception()

        user_claims = AuthUserClaims(
            user_id=current_user.user_id, is_superuser=current_user.is_superuser
        ).dict()
        access_token: str = authorize.create_access_token(
            subject=auth_user.username, user_claims=user_claims, expires_time=settings.ACCESS_TOKEN_EXPIRED
        )
        refresh_token: str = authorize.create_refresh_token(
            subject=auth_user.username, expires_time=settings.ACCESS_TOKEN_EXPIRED
        )
        return JSONResponse({"accessToken": access_token, "refreshToken": refresh_token})
    except (NotFoundError, VerificationFailError):
        raise HTTPException(status_code=422, detail="Bad username or password")
    except Exception as ex:
        logger.exception("error in login: %s", str(ex))
        raise HTTPException(status_code=500, detail="Bad username or password")


@auth_router.post("/refresh")
def refresh(authorize: AuthJWT = Depends()) -> JSONResponse:
    authorize.jwt_refresh_token_required()
    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return JSONResponse({"access_token": new_access_token})


@auth_router.post("/logout")
def logout(authorize: AuthJWT = Depends()) -> None:
    authorize.jwt_required()
