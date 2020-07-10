from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, set_access_cookies, \
    set_refresh_cookies

from src.domain.schemas.user_schemas import user_schema, user_login_schema
from src.domain.services.security_service import SecurityService
from src.http.blueprints.security.controllers import security


@security.route('/login', methods=['POST'])
def get_token_post(security_service: SecurityService):
    json_data = request.get_json()
    user_data = user_login_schema.load(json_data)
    user = security_service.validate_user(user_data.login, user_data.password)

    if user is None:
        return {"msg": "Bad username or password"}, 401

    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)

    resp = jsonify({'login': True,
                    'access_token': access_token,
                    'refresh_token': refresh_token})

    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200


@security.route('/change_password', methods=['POST'])
@jwt_required
def change_password_post(security_service: SecurityService):
    username = request.json.get('username', None)
    new_password = request.json.get('new', None)
    old_password = request.json.get('old', None)
    ret = security_service.change_password(username, old_password, new_password)

    if ret is True:
        return '', 204
    return '', 401
