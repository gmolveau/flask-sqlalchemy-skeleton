# app/api/__init__.py

from flask import Blueprint

root_blueprint = Blueprint('root', __name__)
api_blueprint = Blueprint('api', __name__, url_prefix='/api/')

# Import any endpoints here to make them available
from . import root
from . import examples
