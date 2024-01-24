# backend/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  

app = Flask(__name__)
app.config.from_object('backend.app.config.Config')
db = SQLAlchemy(app)

# Initialize CORS after creating the app instance
CORS(app)

from backend.app import models
from backend.app import routes


