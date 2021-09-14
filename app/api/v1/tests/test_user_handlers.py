import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_users(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/v1/users/all")

    assert response.status_code == 200
    assert response.json() == []
