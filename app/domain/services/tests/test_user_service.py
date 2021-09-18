import pytest

from app.domain.deps import Services
from app.domain.models.user_schemas import CreateUserModel, BaseUserSchema
from app.domain.services.users_service import UserService
from app.domain.types import NotFoundError


@pytest.mark.asyncio
async def test_get_all_users_empty_success() -> None:
    service: UserService = Services.user_service

    result = await service.get_all()
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_by_id_not_found() -> None:
    service: UserService = Services.user_service

    with pytest.raises(NotFoundError):
        await service.get_by_id(1)


@pytest.mark.asyncio
async def test_get_by_id_success() -> None:
    service: UserService = Services.user_service
    repo = Services.user_repository

    user_model = CreateUserModel(nickname="nickname", email="test@test.com", password="passwd")
    await repo.create(user_model)

    result = await service.get_by_id(1)

    assert result.user_id == 1


@pytest.mark.asyncio
async def test_create_user_success() -> None:
    service: UserService = Services.user_service

    user_model = CreateUserModel(nickname="nickname", email="test@test.com", password="passwd")
    result = await service.create(user_model)

    assert result.user_id == 1
    assert result.nickname == user_model.nickname
    assert result.email == user_model.email


@pytest.mark.asyncio
async def test_ban_user_success() -> None:
    service: UserService = Services.user_service
    repo = Services.user_repository

    await repo.create(CreateUserModel(nickname="nickname", email="test@test.com", password="passwd"))

    await service.ban_user(1)

    user = await repo.get_by_id(1)
    assert user.is_active is False


@pytest.mark.asyncio
async def test_unban_user_success() -> None:
    service: UserService = Services.user_service
    repo = Services.user_repository

    created_result = await repo.create(CreateUserModel(nickname="nickname", email="test@test.com", password="passwd"))
    updated_model = BaseUserSchema(**created_result.__dict__["__values__"])
    updated_model.is_active = False
    await repo.update(created_result, updated_model)

    await service.unban_user(1)

    user = await repo.get_by_id(1)
    assert user.is_active is True
