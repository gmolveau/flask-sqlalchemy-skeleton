# tests/conftest.py

import pytest
from dotenv import load_dotenv
load_dotenv()

from app import create_app
from app.database import db


@pytest.fixture(scope="session")
def global_data():
    return dict()


@pytest.fixture(scope="session")
def client():
    # setup
    test_app = create_app()

    from os import environ as env
    test_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.sqlite"
    test_app.config['TESTING'] = True
    client = test_app.test_client()

    with test_app.app_context():
        db.drop_all()
        db.create_all()

    yield client

    # teardown
    with test_app.app_context():
        pass
        #db.drop_all()
