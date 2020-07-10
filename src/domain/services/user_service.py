import bcrypt
from injector import inject

from src.domain.models.users import User
from src.domain.repositories.user_repository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self):
        return self.user_repository.get_all()

    def get_by_login(self, login):
        return self.user_repository.get_by_login(login)

    def create_user(self, user: User):
        user.password = bcrypt.hashpw(user.password, bcrypt.gensalt())
        return self.user_repository.create(user)

    def change_password(self, username, new_password):
        new_password = bcrypt.hashpw(new_password, bcrypt.gensalt())
        return self.user_repository.change_password(username, new_password)
