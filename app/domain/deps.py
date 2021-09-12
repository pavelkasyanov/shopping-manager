from dependency_injector import containers, providers

from app.domain.repositories.user_repository import UserRepository
from app.domain.services.users_service import UserService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository = providers.Factory(UserRepository)

    user_service = providers.Factory(
        UserService, user_repository=user_repository
    )
