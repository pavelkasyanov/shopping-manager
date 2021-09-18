from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from .depends import get_authentication_service
from .models import AuthUser
from ...domain.models.auth_user_claims import AuthUserClaims
from ...domain.services.authentication_service import AuthenticationService

auth_router = APIRouter()


@auth_router.post("/login")
async def login(
    auth_user: AuthUser,
    authorize: AuthJWT = Depends(),
    authentication_service: AuthenticationService = Depends(
        get_authentication_service
    ),
):
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
            subject=auth_user.username, user_claims=user_claims
        )
        refresh_token: str = authorize.create_refresh_token(
            subject=auth_user.username
        )
        return {"access_token": access_token, "refresh_token": refresh_token}
    except Exception as ex:
        raise HTTPException(status_code=401, detail="Bad username or password")


@auth_router.post("/refresh")
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()
    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@auth_router.post("/logout")
def logout(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
