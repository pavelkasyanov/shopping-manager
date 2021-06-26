import pytest
from httpx import AsyncClient

from app.app import app


@pytest.fixture
async def async_client():
    with AsyncClient(app=app, base_url="http://test") as client:
        yield client
