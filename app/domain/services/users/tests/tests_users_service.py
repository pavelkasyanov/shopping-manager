import pytest
from httpx import AsyncClient

from app.domain.models.users import CreateUserViewModel
from app.domain.services.users.users_service import UsersService


@pytest.mark.asyncio
async def test_create_user_success(async_client: AsyncClient) -> None:
    user_service = UsersService()

    user_vm = CreateUserViewModel(
        nickname="test_user", email="test_user@mail.com"
    )

    created_user = user_service.create(user_vm)

    assert created_user is not None
    assert created_user.id is not None
    assert created_user.nickname == user_vm.nickname
