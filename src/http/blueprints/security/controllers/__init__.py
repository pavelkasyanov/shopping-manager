from flask import Blueprint

security = Blueprint('security', __name__)

import src.http.blueprints.security.controllers.security_controller
import src.http.blueprints.security.controllers.user_controller
