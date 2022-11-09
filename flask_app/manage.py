import click
from flask import Blueprint
from flask_app.models import db


cli = Blueprint('db', __name__)


@cli.cli.command('create_db')
def create():
    """ Creates the database """
    db.create_all()
    print('Database created')


@cli.cli.command('reset_db')
def reset():
    """ Delete the current database and recreate """
    db.drop_all()
    db.session.commit()
    db.create_all()
    print('Database recreated')


