from typing import Any, Dict

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_login_success(auth_client: AsyncClient):
    data: Dict[str, Any] = {"username": "test", "password": "test"}
    response = await auth_client.post("/login", json=data)
    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["refresh_token"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "login,password", (("test", ""), ("", "test"), ("123", ""), ("", "123"))
)
async def test_invalid_login(
    async_client: AsyncClient, login: str, password: str
):
    data: Dict[str, Any] = {"username": login, "password": password}
    response = await async_client.post("/login", json=data)
    assert response.status_code == 401
