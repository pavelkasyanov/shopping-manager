from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class USerSchema(BaseModel):
    user_id: int
    email: Optional[EmailStr] = Field(default=None)
    is_active: Optional[bool] = Field(default=True)
    is_superuser: Optional[bool] = Field(default=False)
    full_name: Optional[str] = Field(default=None)


class CreateModel(BaseModel):
    nickname: str
    email: str
    password: str
