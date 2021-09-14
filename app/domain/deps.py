from typing import cast

from dependencies import Injector

from app.domain.repositories.user_repository import UserRepository
from app.domain.services.users_service import UserService


class Services(Injector):
    user_repository = cast(UserRepository, UserRepository)
    user_service = cast(UserService, UserService)
