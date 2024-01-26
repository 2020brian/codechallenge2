from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.routes import restaurant_bp, pizza_bp
from app.models.models import db
from app import app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)
