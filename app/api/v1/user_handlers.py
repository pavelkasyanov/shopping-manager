from typing import List

from fastapi import APIRouter, Depends

from dependency_injector.wiring import Provide, inject

from app.domain.deps import Container
from app.domain.models.user_schemas import UserSchema
from app.domain.services.users_service import UserService

router = APIRouter(prefix="/users")


@router.get("/all", name="get_all_users")
@inject
async def get_all_users(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> List[UserSchema]:
    return await user_service.get_all()


@router.get("/{user_id}", name="get_user_by_id")
async def get_user_by_id(
    user_service=Depends(Provide[Container.user_service]),
) -> None:
    pass


@router.post("/create", name="create_user")
async def create_user(
    user_service=Depends(Provide[Container.user_service]),
) -> None:
    pass


@router.post("/ban", name="create_user")
async def ban_user(
    user_service=Depends(Provide[Container.user_service]),
) -> None:
    pass


@router.post("/unban", name="create_user")
async def unban_user(
    user_service=Depends(Provide[Container.user_service]),
) -> None:
    pass
