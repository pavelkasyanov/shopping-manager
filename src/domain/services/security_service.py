import bcrypt
from injector import inject

from src.domain.exceptions.user_exceptions import UserNotFound, PasswordNotCheck
from src.domain.services.user_service import UserService


class SecurityService:
    @inject
    def __init__(self, user_service: UserService) -> None:
        super().__init__()
        self.user_service = user_service

    def validate_user(self, login, password):
        found = self.user_service.get_by_login(login)
        if found is None:
            raise UserNotFound(login)

        if not bcrypt.checkpw(password, found.password):
            raise PasswordNotCheck()

        return found

    def change_password(self, username, old_password, new_password):
        self.validate_user(username, old_password)
        return self.user_service.change_password(username, new_password)
