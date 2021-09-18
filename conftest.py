import pytest

from app.infrastructure.database.db import db

pytest_plugins = [
    "app.tests.fixtures.client",
]


@pytest.mark.asyncio
@pytest.fixture(autouse=True, scope="function")
async def init_db() -> None:
    await db.set_bind(
        db.config["dsn"],
        echo=db.config["echo"],
        min_size=db.config["min_size"],
        max_size=db.config["max_size"],
        ssl=db.config["ssl"],
        **db.config["kwargs"],
    )
    await db.gino.create_all()
    yield
    await db.gino.drop_all()
