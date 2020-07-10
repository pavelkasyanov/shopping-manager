from flask import Blueprint

api = Blueprint('api', __name__)

import src.http.blueprints.api.controllers.help.help_controller
