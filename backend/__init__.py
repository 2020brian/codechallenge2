from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend import routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    # Enable CORS for all routes
    CORS(app)

    # Initialize SQLAlchemy
    db.init_app(app)

    return app
