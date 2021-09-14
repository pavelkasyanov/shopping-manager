from typing import List

from fastapi import APIRouter, Depends

from app.api.deps import get_user_service
from app.domain.models.user_schemas import UserSchema, CreateUserModel
from app.domain.services.users_service import UserService
from app.domain.types import UserId

router = APIRouter(prefix="/users")


@router.get("/all", name="get_all_users", status_code=200)
async def get_all_users(
    user_service: UserService = Depends(get_user_service),
) -> List[UserSchema]:
    return await user_service.get_all()


@router.get("/{user_id}", name="get_user_by_id", status_code=200)
async def get_user_by_id(
    user_id: UserId,
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.get_by_id(user_id)


@router.post("/create", name="create_user", status_code=201)
async def create_user(
    create_model: CreateUserModel,
    user_service: UserService = Depends(get_user_service),
) -> UserSchema:
    return await user_service.create(create_model)


@router.post("/{user_id}/ban", name="create_user", status_code=204)
async def ban_user(
    user_id: UserId,
    user_service: UserService = Depends(get_user_service),
) -> None:
    await user_service.ban_user(user_id)


@router.post("/{user_id}/unban", name="create_user", status_code=204)
async def unban_user(
    user_id: UserId,
    user_service: UserService = Depends(get_user_service),
) -> None:
    await user_service.unban_user(user_id)
