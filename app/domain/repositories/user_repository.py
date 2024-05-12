from typing import List

from app.domain.models.user_schemas import BaseUserSchema, CreateUserModel
from app.domain.types import NotFoundError, UserId
from app.infrastructure.database.models.user import User


class UserRepository:
    _model = User

    async def get_all(self) -> List[User]:
        return await self._model.query.gino.all()

    async def get_by_id(self, user_id: UserId) -> User:
        user = await self._model.get(user_id)
        if not user:
            raise NotFoundError()
        return user

    async def get_by_email(self, user_email: str) -> User:
        user = await User.query.where(User.email == user_email).gino.first()
        if not user:
            raise NotFoundError()
        return user

    async def create(self, user_model: CreateUserModel) -> User:
        return await self._model.create(**user_model.__dict__)

    @classmethod
    async def update(cls, old_user: User, new_user: BaseUserSchema) -> User:
        user_updated = await old_user.update(**new_user.__dict__).apply()
        return user_updated._instance
