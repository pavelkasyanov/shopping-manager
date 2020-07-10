from flask import Blueprint

index = Blueprint('index', __name__)

import src.http.blueprints.index.controllers.index_controller
