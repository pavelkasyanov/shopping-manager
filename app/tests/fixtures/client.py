import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy_utils import database_exists, create_database, drop_database

from app.app import app
from settings import settings


@pytest.fixture
async def async_client():

    if database_exists(settings.DB_DSN):
        drop_database(settings.DB_DSN)
    create_database(settings.DB_DSN)

    async with AsyncClient(
        app=app, base_url="http://test"
    ) as client, LifespanManager(app):
        yield client
