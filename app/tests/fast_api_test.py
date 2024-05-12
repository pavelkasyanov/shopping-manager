import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ping(async_client: AsyncClient):
    response = await async_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}


@pytest.mark.asyncio
async def test_404(async_client: AsyncClient):
    response = await async_client.get("/test-url")
    assert response.status_code == 404
