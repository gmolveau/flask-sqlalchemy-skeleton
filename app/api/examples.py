# app/api/example.py

from flask import (
    request
)
from . import api_blueprint
from ..database import db
from ..models.example import Example


@api_blueprint.route('/examples', methods=['GET'])
def get_all():
    examples = Example.query.all()
    return "all records"
