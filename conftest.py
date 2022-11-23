import pytest
import alembic
from alembic import command
from alembic.config import Config
from sqlalchemy_utils import database_exists, create_database, drop_database

from app.infrastructure.database.db import db
from settings import settings

alembic_config = Config("alembic.ini")

pytest_plugins = [
    "app.tests.fixtures.client",
]


@pytest.mark.asyncio
@pytest.fixture(autouse=True)
async def create_db() -> None:
    await db.set_bind(
        db.config["dsn"],
        echo=db.config["echo"],
        min_size=db.config["min_size"],
        max_size=db.config["max_size"],
        ssl=db.config["ssl"],
        **db.config["kwargs"],
    )
    command.upgrade(alembic_config, "head")
    yield
    await db.pop_bind().close()
    command.downgrade(alembic_config, "base")


def pytest_configure(config):
    if not database_exists(settings.DB_DSN):
        create_database(settings.DB_DSN)


def pytest_unconfigure(config):
    drop_database(settings.DB_DSN)
