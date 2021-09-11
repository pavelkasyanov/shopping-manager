from typing import List, Optional

from app.domain.models.users.user_schemas import UserSchema
from app.domain.types import UserId, UserNotExistError
from app.infrastructure.database.models.user import User


class UserRepository:
    _model = User

    async def get_all(self) -> List[UserSchema]:
        users = await self._model.all()
        return [UserSchema.from_orm(x) for x in users]

    async def get_by_id(self, user_id: UserId) -> Optional[UserSchema]:
        user = await self._model.get(user_id)
        if not user:
            raise UserNotExistError()
        return UserSchema.from_orm(user)

    async def create(self) -> UserSchema:
        pass