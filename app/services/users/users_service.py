from typing import List, Union

from app.models.db.auth.users import User
from app.models.view_models.users.create_user_vm import CreateUserViewModel


class UsersService:

    @classmethod
    async def get_all(cls) -> List[User]:
        return await User.all()

    @classmethod
    async def get_by_id(cls, user_id: int) -> Union[User, None]:
        user = await User.get(user_id)
        if not user:
            return None
        return user

    @classmethod
    async def create(cls, user_vm: CreateUserViewModel) -> User:
        user = await User.create(nickname=user_vm.nickname, is_baned=False, email=user_vm.email)
        return user
