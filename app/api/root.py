# app/api/root.py

from flask import (
    request, render_template
)
from . import root_blueprint
from .decorators import decorator


@root_blueprint.route('/', methods=['GET'])
@decorator
def index(added_data):
    # added_data comes from the decorator
    return render_template("index.html")
