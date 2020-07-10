from flask import jsonify
from flask_jwt_extended import jwt_required

from src.http.blueprints.api.controllers import api
from version import __app_version__ as app_version


@api.route('/version', methods=['GET'])
@jwt_required
def get_version():
    return jsonify(app_version), 200
