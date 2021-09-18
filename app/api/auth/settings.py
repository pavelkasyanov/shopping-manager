from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class AuthSettings(BaseModel):
    authjwt_secret_key: str = "6781a726a85e4e62ad8d85580c8a2f8d"
    authjwt_token_location: set = {"headers"}
    authjwt_cookie_csrf_protect: bool = True


@AuthJWT.load_config
def get_config():
    return AuthSettings()
