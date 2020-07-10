from marshmallow import Schema, fields, post_load

from src.domain.models.users import User
from src.domain.schemas.base_schema import BaseSchema


class UserRoleSchema(BaseSchema):
    id = fields.UUID()
    type = fields.Str()


class UserSchema(BaseSchema):
    id = fields.UUID(required=False)
    login = fields.Str()
    password = fields.Str()
    email = fields.Email()
    role_id = fields.UUID(load_from="roleId")

    @post_load
    def make_user(self, data, **kwargs):
        data['password'] = data['password'].encode("utf8")
        return User(**data)


user_login_schema = UserSchema(many=False, only=('login', 'password'))
user_schema = UserSchema(exclude=('password',))
users_schema = UserSchema(many=True, exclude=('password',))