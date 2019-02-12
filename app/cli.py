# app/cli.py

import click
from flask.cli import with_appcontext
from .database import db
from .models.example import Example


@click.command('reset-db')
@with_appcontext
def reset_db_command():
    """Clear existing data and create new tables."""
    # run it with : FLASK_APP=. flask reset-db
    db.drop_all()
    db.create_all()
    click.echo('The database has been reset.')

def cli_init_app(app):
    app.cli.add_command(reset_db_command)
