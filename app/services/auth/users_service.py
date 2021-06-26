from typing import List

from app.models.db.auth.users import User


class UsersService:

    @classmethod
    async def get_all(cls) -> List[User]:
        return await User.all()
