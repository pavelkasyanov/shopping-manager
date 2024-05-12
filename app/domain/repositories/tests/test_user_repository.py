import pytest as pytest

from app.domain.deps import Services
from app.domain.models.user_schemas import BaseUserSchema, CreateUserModel
from app.infrastructure.database.models.user import User


async def create_user(
    nickname: str = "test",
    email: str = "test@test.com",
    password: str = "passwd",
) -> User:
    repo = Services.user_repository
    user_model = CreateUserModel(nickname=nickname, email=email, password=password)
    return await repo.create(user_model)


@pytest.mark.asyncio
async def test_gel_all_users_empty_success() -> None:
    repo = Services.user_repository

    result = await repo.get_all()
    assert len(result) == 0


@pytest.mark.asyncio
async def test_create_user_success() -> None:
    create_result = await create_user()

    assert create_result is not None
    assert create_result.user_id is not None


@pytest.mark.asyncio
async def test_gel_all_users_success() -> None:
    repo = Services.user_repository

    create_result = await create_user()

    result = await repo.get_all()
    assert len(result) == 1

    assert result[0].user_id == create_result.user_id


@pytest.mark.asyncio
async def test_update_user() -> None:
    repo = Services.user_repository

    create_result: User = await create_user()

    new_user = BaseUserSchema(**create_result.__dict__["__values__"])
    new_user.is_superuser = True

    update_result = await repo.update(create_result, new_user)

    assert update_result is not None
    assert update_result.is_superuser is True
