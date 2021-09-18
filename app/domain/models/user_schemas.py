from typing import Optional

from pydantic.fields import Field
from pydantic.networks import EmailStr

from app.domain.models.base import Entity


class BaseUserSchema(Entity):
    user_id: int
    email: Optional[EmailStr] = Field(default=None)
    is_active: Optional[bool] = Field(default=True)
    is_superuser: Optional[bool] = Field(default=False)

    class Config:
        orm_mode = True


class CreateUserModel(Entity):
    nickname: str
    email: str
    password: str


class UserSchema(BaseUserSchema):
    user_id: int
