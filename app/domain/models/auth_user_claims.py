from pydantic.fields import Field
from pydantic.main import BaseModel

from app.domain.types import UserId


class AuthUserClaims(BaseModel):
    user_id: UserId
    is_superuser: bool = Field(default=False)
