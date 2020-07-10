import datetime

from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector
from sqlalchemy import create_engine
from werkzeug.routing import ValidationError

from src.domain import Session, Base
from src.http import jwt, jsglue
from src.http.blueprints.api.controllers import api
from src.http.blueprints.index import index
from src.http.blueprints.security.controllers import security
from src.http.error_handlers import err_404, err_405, err_500, err_validation
from src.http.jwt_handlers import add_claims_to_access_token, user_identity_lookup

app = Flask(__name__)


def create_app(database_url, testing: bool = False):
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['CSRF_ENABLED'] = True
    app.config['JWT_COOKIE_SECURE'] = False
    app.config['SECRET_KEY'] = 'this-really-needs-to-be-changed'
    app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = True
    app.config['TESTING'] = testing

    engine = create_engine(database_url, pool_size=100, max_overflow=120)
    Session.configure(bind=engine, expire_on_commit=False)
    Base.metadata.bind = engine

    jwt.init_app(app)
    jwt.user_claims_loader(add_claims_to_access_token)
    jwt.user_identity_loader(user_identity_lookup)

    jsglue.init_app(app)

    app.register_error_handler(404, err_404)
    app.register_error_handler(405, err_405)
    app.register_error_handler(500, err_500)
    app.register_error_handler(Exception, err_500)
    app.register_error_handler(ValidationError, err_validation)

    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(security, url_prefix='/security')

    injector = Injector()
    FlaskInjector(app=app, injector=injector, modules=[configure])

    return app


def configure(binder):
    pass

@app.teardown_appcontext
def cleanup(resp_or_exc):
    pass
