from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.routes import restaurant_bp, pizza_bp
import os

app = Flask(__name__)

# Use environment variable for database URI (update 'REPLACE_WITH_RENDER_DB_URL' with the actual environment variable name on Render)
DATABASE_URI = os.environ.get('REPLACE_WITH_RENDER_DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)
