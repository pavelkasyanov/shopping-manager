from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


async def auth_user(authorize: AuthJWT = Depends()) -> object:
    authorize.jwt_required()
    current_user = authorize.get_jwt_subject()
    return current_user
