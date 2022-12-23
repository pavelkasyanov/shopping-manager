from typing import Union

from passlib.hash import pbkdf2_sha256

from app.domain.models.user_schemas import VerificationUserSchema
from app.domain.services.users_service import UserService
from app.domain.types import VerificationFailError


class AuthenticationService:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    async def verify_user(
        self, login: str, passwd: str
    ) -> Union[VerificationUserSchema, None]:
        current_user = await self._user_service.get_for_verification(login)

        if not pbkdf2_sha256.verify(passwd, current_user.password):
            raise VerificationFailError()

        return VerificationUserSchema.from_orm(current_user)

    @classmethod
    async def create_hash_by_password(cls, passwd: str) -> str:
        return pbkdf2_sha256.hash(passwd)
