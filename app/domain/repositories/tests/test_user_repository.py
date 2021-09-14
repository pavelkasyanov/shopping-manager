import pytest as pytest

from httpx import AsyncClient

from app.domain.deps import Services


@pytest.mark.asyncio
async def test_gel_all_users(async_client: AsyncClient) -> None:
    repo = Services.user_repository

    result = await repo.get_all()
    assert len(result) == 0
