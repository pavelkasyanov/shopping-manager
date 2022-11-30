from typing import List

from app.domain.models.user_schemas import (
    CreateUserModel,
    UserSchema,
    VerificationUserSchema,
)
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
        user = await self._user_repository.get_by_id(user_id)
        return UserSchema.from_orm(user)

    async def get_by_email(self, email: str) -> UserSchema:
        user = await self._user_repository.get_by_email(email)
        return UserSchema.from_orm(user)

    async def create(self, user_model: CreateUserModel) -> User:
        return await self._user_repository.create(user_model=user_model)

    async def ban_user(self, user_id: UserId) -> None:
        await self._set_banned_status(user_id, True)

    async def unban_user(self, user_id: UserId) -> None:
        await self._set_banned_status(user_id, False)

    async def get_for_verification(self, login: str) -> VerificationUserSchema:
        user = await self._user_repository.get_by_email(login)
        return VerificationUserSchema.from_orm(user)

    async def _set_banned_status(self, user_id: UserId, status: bool) -> None:
        current_user = await self._user_repository.get_by_id(user_id)
        current_schema = UserSchema.from_orm(current_user)
        current_schema.is_banned = status
        await self._user_repository.update(
            current_user, new_user=current_schema
        )
