from datetime import datetime
from typing import Optional

from pydantic.fields import Field
from pydantic.networks import EmailStr

from app.domain.models.base import Entity


class BaseUserSchema(Entity):
    nickname: str = Field(alias="nickname")
    email: Optional[EmailStr] = Field(default=None, alias="email")
    is_banned: Optional[bool] = Field(default=True, alias="isBanned")
    is_superuser: Optional[bool] = Field(default=False, alias="isSuperUser")

    class Config:
        orm_mode = True


class CreateUserModel(Entity):
    nickname: str
    email: str
    password: str


class UserSchema(BaseUserSchema):
    user_id: int = Field(alias="userId")
    created_date: datetime = Field(alias="created")


class VerificationUserSchema(UserSchema):
    password: str
