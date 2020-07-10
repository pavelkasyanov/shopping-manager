from flask import jsonify, render_template
from flask_jwt_extended import jwt_required

from src.domain.schemas.user_schemas import users_schema
from src.domain.services.user_service import UserService
from src.http.blueprints.security.controllers import security


@security.route('/users')
@jwt_required
def get_user_index():
    return render_template('users.html', name='gfg')


@security.route('/users/all', methods=['GET'])
@jwt_required
def get_all_users(user_service: UserService):
    users = user_service.get_users()
    result = users_schema.dump(users).data

    obj = {
        "totalCount": len(result),
        "items": result
    }

    return jsonify(obj), 200
