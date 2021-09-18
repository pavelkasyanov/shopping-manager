from typing import List

from fastapi import APIRouter, Depends

from app.api.deps import (
    get_user_service,
    get_authorized_superuser,
    get_authorized_user,
)
from app.domain.models.auth_user_claims import AuthUserClaims
from app.domain.models.user_schemas import UserSchema, CreateUserModel
from app.domain.services.users_service import UserService
from app.domain.types import UserId

router = APIRouter(prefix="/users")


@router.get("/all", name="get_all_users", status_code=200)
async def get_all_users(
    auth_user: AuthUserClaims = Depends(get_authorized_superuser),
    user_service: UserService = Depends(get_user_service),
) -> List[UserSchema]:
    return await user_service.get_all()


@router.get("/me", name="get_user_info_about_me", status_code=200)
async def get_current_user(
    auth_user: AuthUserClaims = Depends(get_authorized_user),
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.get_by_id(auth_user.user_id)


@router.get("/{user_id}", name="get_user_by_id", status_code=200)
async def get_user_by_id(
    user_id: UserId,
    auth_user: AuthUserClaims = Depends(get_authorized_superuser),
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.get_by_id(user_id)


@router.post("/create", name="create_user", status_code=201)
async def create_user(
    create_model: CreateUserModel,
    auth_user: AuthUserClaims = Depends(get_authorized_superuser),
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.create(create_model)


@router.post("/{user_id}/ban", name="create_user", status_code=204)
async def ban_user(
    user_id: UserId,
    auth_user: AuthUserClaims = Depends(get_authorized_superuser),
    user_service: UserService = Depends(get_user_service),
) -> None:
    await user_service.ban_user(user_id)


@router.post("/{user_id}/unban", name="create_user", status_code=204)
async def unban_user(
    user_id: UserId,
    user_service: UserService = Depends(get_user_service),
) -> None:
    await user_service.unban_user(user_id)
