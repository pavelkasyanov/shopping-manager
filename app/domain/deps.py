from dependency_injector import containers, providers
from services.users import users_service as users


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_service = providers.Factory(
        users.UsersService
    )
