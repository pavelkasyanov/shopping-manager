from typing import List

from app.domain.models.user_schemas import CreateUserModel, UserSchema
from app.domain.repositories.user_repository import UserRepository
from app.domain.types import UserId
from app.infrastructure.database.models.user import User


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    async def get_all(self) -> List[UserSchema]:
        users = await self._user_repository.get_all()
        return [UserSchema.from_orm(x) for x in users]

    async def get_by_id(self, user_id: UserId) -> UserSchema:
        return await self._user_repository.get_by_id(user_id)

    async def create(self, user_model: CreateUserModel) -> User:
        return await self._user_repository.create(user_model=user_model)
