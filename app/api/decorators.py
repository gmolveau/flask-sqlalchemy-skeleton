# app/api/decorators.py

from functools import wraps
from flask import (
    request, Response
)

def decorator(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        # do things here like
        added_data = "i am passed to the decorated function"
        return fn(added_data, *args, **kwargs)
    return decorated
