from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT

from .models import AuthUser

auth_router = APIRouter()


@auth_router.post("/login")
def login(auth_user: AuthUser, authorize: AuthJWT = Depends()):
    if auth_user.username != "test" or auth_user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token: str = authorize.create_access_token(
        subject=auth_user.username
    )
    refresh_token = authorize.create_refresh_token(subject=auth_user.username)
    return {"access_token": access_token, "refresh_token": refresh_token}


@auth_router.post("/refresh")
def refresh(authorize: AuthJWT = Depends()):
    authorize.jwt_refresh_token_required()
    current_user = authorize.get_jwt_subject()
    new_access_token = authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@auth_router.post("/logout")
def logout(authorize: AuthJWT = Depends()):
    authorize.jwt_required()
