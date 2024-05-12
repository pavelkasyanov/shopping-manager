from typing import Any, AsyncGenerator

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.infrastructure.database.db import db
from settings import settings

alembic_config = Config("alembic.ini")

pytest_plugins = ["app.tests.fixtures.client", "app.domain.repositories.tests.fixtures"]


@pytest.mark.asyncio
@pytest.fixture(autouse=True)
async def create_db() -> AsyncGenerator[None, None]:
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


def pytest_configure(config: Any) -> None:
    if not database_exists(settings.DB_DSN):
        create_database(settings.DB_DSN)


def pytest_unconfigure(config: Any) -> None:
    drop_database(settings.DB_DSN)
