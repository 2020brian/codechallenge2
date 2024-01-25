# backend/manage.py
from flask.cli import FlaskGroup
from backend.wsgi import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
