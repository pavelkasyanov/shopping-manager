import os
from typing import Optional

from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret


class AppSettings:
    def __init__(self, conf_filename: Optional[str] = None):
        config = Config(env_file=conf_filename or ".env", environ=os.environ)

        self.TESTING = config("TESTING", cast=bool, default=False)

        self.DB_DRIVER = config("DB_DRIVER", default="postgresql")
        self.DB_HOST = config("DB_HOST")
        self.DB_PORT = config("DB_PORT", cast=int)
        self.DB_USER = config("DB_USER")
        self.DB_PASSWORD = config("DB_PASSWORD", cast=Secret)
        self.DB_DATABASE = config("DB_DATABASE")
        if self.TESTING:
            if self.DB_DATABASE:
                self.DB_DATABASE += "-test"
            else:
                self.DB_DATABASE = "shopping-manager-test"
        self.DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
        self.DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=16)
        self.DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=16)
        self.DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)
        self.DB_DSN = config(
            "DB_DSN",
            cast=make_url,
            default=URL(
                drivername=self.DB_DRIVER,
                username=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT,
                database=self.DB_DATABASE,
            ),
        )
        self.DB_ECHO = config("DB_ECHO", cast=bool, default=False)

        self.DEBUG = config("DEBUG", cast=bool, default=False)

        self.SITE_URL = config("SITE_URL", default="0.0.0.0")

        self.ACCESS_TOKEN_EXPIRED = config("ACCESS_TOKEN_EXPIRED", cast=int, default=15)


settings = AppSettings()
