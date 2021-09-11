import os
from typing import Optional, Any, Callable

from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret


def get_value(
    config: Config, key: str, cast: Callable = None, default_value: Any = None
) -> Any:
    return config(key, cast=cast, default=default_value) or os.environ.get(
        "DB_DRIVER", default=default_value
    )


class AppSettings:
    def __init__(self, conf_filename: Optional[str] = None):
        config = Config(conf_filename or ".env")

        self.TESTING = get_value(
            config, "TESTING", cast=bool, default_value=False
        )

        self.DB_DRIVER = get_value(
            config, "DB_DRIVER", default_value="postgresql"
        )
        self.DB_HOST = get_value(config, "DB_HOST")
        self.DB_PORT = get_value(config, "DB_PORT", cast=int)
        self.DB_USER = get_value(config, "DB_USER")
        self.DB_PASSWORD = get_value(config, "DB_PASSWORD", cast=Secret)
        self.DB_DATABASE = get_value(config, "DB_DATABASE")
        if self.TESTING:
            if self.DB_DATABASE:
                self.DB_DATABASE += "_test"
            else:
                self.DB_DATABASE = "shopping_manager_test"
        self.DB_POOL_MIN_SIZE = get_value(
            config, "DB_POOL_MIN_SIZE", cast=int, default_value=1
        )
        self.DB_POOL_MAX_SIZE = get_value(
            config, "DB_POOL_MAX_SIZE", cast=int, default_value=16
        )
        self.DB_RETRY_LIMIT = get_value(
            config, "DB_RETRY_LIMIT", cast=int, default_value=16
        )
        self.DB_RETRY_INTERVAL = get_value(
            config, "DB_RETRY_INTERVAL", cast=int, default_value=1
        )

        self.DB_DSN = get_value(
            config,
            "DB_DSN",
            cast=make_url,
            default_value=URL(
                drivername=self.DB_DRIVER,
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                database=self.DB_DATABASE,
            ),
        )
        self.DB_ECHO = get_value(
            config, "DB_ECHO", cast=bool, default_value=False
        )

        self.DEBUG = get_value(config, "DEBUG", cast=bool, default_value=False)

        self.SITE_URL = get_value(config, "SITE_URL")


settings = AppSettings()
