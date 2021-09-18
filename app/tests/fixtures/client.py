import pytest
from httpx import AsyncClient

from app.app import app


@pytest.fixture
async def async_client():
    client = AsyncClient(app=app, base_url="http://test.by")
    yield client
    await client.aclose()
