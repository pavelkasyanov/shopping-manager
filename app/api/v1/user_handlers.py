from fastapi import APIRouter, Depends

from dependency_injector.wiring import Provide

from app.domain.deps import Container

router = APIRouter(prefix="/users")


@router.get("/all", name="get_all_users")
async def get_all_users(user_service=Depends(Provide[Container.user_service])) -> None:
    pass


@router.get("/{user_id}", name="get_user_by_id")
async def get_user_by_id(user_service=Depends(Provide[Container.user_service])) -> None:
    pass


@router.post("/create", name="create_user")
async def create_user(user_service=Depends(Provide[Container.user_service])) -> None:
    pass


@router.post("/ban", name="create_user")
async def ban_user(user_service=Depends(Provide[Container.user_service])) -> None:
    pass


@router.post("/unban", name="create_user")
async def unban_user(user_service=Depends(Provide[Container.user_service])) -> None:
    pass
