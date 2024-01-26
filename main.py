from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes.routes import restaurant_bp, pizza_bp
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)


DATABASE_URI = os.environ.get('REPLACE_WITH_RENDER_DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI


db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)

if __name__ == '__main__':
    app.run(debug=True)
