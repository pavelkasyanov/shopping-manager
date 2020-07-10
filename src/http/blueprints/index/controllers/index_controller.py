from flask import jsonify, render_template
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required

from src.http.blueprints.index import index
from src.logger import logger


@index.route('', methods=['GET'])
@jwt_optional
def get_index():
    current_user = get_jwt_identity()
    if current_user:
        logger.info('user authorized, show index page')
        return render_template('index.html')
    else:
        logger.info('user not authorized, show login page')
        return render_template('login.html')
