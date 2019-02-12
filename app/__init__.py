# app/__init__.py

from flask import Flask
from os import environ as env

def create_app():
    app = Flask(__name__)
    check_env(app.logger)

    app.config['SQLALCHEMY_DATABASE_URI'] = env.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .database import db
    db.init_app(app)

    from .cli import cli_init_app
    cli_init_app(app)

    from .api import api_blueprint, root_blueprint
    app.register_blueprint(root_blueprint)
    app.register_blueprint(api_blueprint)

    return app

def check_env(logger):
    for var in ['DATABASE_URL', 'AUTH_USERNAME', 'AUTH_PASSWORD']:
        if env.get(var) is None:
            logger.error('environment variable {0} is not set.'.format(var))
