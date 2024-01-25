from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    # Enable CORS for all routes
    CORS(app)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Import routes after initializing the app to avoid circular import
    from backend import routes

    return app
