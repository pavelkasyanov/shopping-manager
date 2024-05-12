import datetime

import pytest
from httpx import AsyncClient

from app.domain.models.user_schemas import UserSchema
from app.domain.services.users_service import UserService
from app.domain.types import NotFoundError


@pytest.mark.asyncio
async def test_get_all_users_not_authorized(async_client: AsyncClient, mocker) -> None:
    mocker.patch.object(UserService, "get_all", return_value=[])

    response = await async_client.get("/api/v1/users/all", headers={"Content-Type": "application/json"})

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_all_users_forbidden(auth_client: AsyncClient, mocker) -> None:
    mocker.patch.object(UserService, "get_all", return_value=[])

    response = await auth_client.get("/api/v1/users/all")

    assert response.status_code == 403


@pytest.mark.asyncio
async def test_get_all_users_success(auth_superuser_client: AsyncClient, mocker) -> None:
    mocker.patch.object(
        UserService,
        "get_all",
        return_value=[
            UserSchema.parse_obj(
                {
                    "user_id": 1,
                    "email": "test@test.by",
                    "created_date": datetime.datetime.utcnow(),
                    "nickname": "test_nickname",
                }
            )
        ],
    )

    response = await auth_superuser_client.get("/api/v1/users/all")

    assert response.status_code == 200
    assert response.json() is not None
    response_json = response.json()
    assert len(response_json) == 1
    assert response_json[0]["userId"] == 1
    assert response_json[0]["email"] == "test@test.by"
    assert response_json[0]["nickname"] == "test_nickname"


@pytest.mark.asyncio
async def test_get_user_by_id_success(auth_superuser_client: AsyncClient, mocker) -> None:
    mocker.patch.object(
        UserService,
        "get_by_id",
        return_value=[
            UserSchema(
                user_id=1,
                email="test@test.by",
                created_date=datetime.datetime.utcnow(),
                nickname="test_nickname",
            )
        ],
    )

    response = await auth_superuser_client.get("/api/v1/users/1")

    assert response.status_code == 200
    assert response.json() is not None
    response_json = response.json()
    assert len(response_json) == 1
    assert response_json[0]["userId"] == 1
    assert response_json[0]["email"] == "test@test.by"
    assert response_json[0]["nickname"] == "test_nickname"


@pytest.mark.asyncio
async def test_get_user_by_id_not_found_error(auth_superuser_client: AsyncClient, mocker) -> None:
    async def response(user_id) -> None:
        raise NotFoundError()

    mocker.patch.object(UserService, "get_by_id", side_effect=response)

    with pytest.raises(NotFoundError):
        await auth_superuser_client.get("/api/v1/users/2")
