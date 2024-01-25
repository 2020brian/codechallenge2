from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.app.config.Config')

    from backend.app import routes  # Import inside create_app
    db.init_app(app)

    return app
