
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('backend.app.config.Config')
db = SQLAlchemy(app)


from backend.app import models


from backend.app import routes
