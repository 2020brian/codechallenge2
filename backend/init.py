# backend/app/__init__.py
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    api = Api(app)

    # Import resources and add them to the API
    from .routes import RestaurantListResource, RestaurantResource, PizzaListResource, RestaurantPizzaResource
    api.add_resource(RestaurantListResource, '/api/restaurants')
    api.add_resource(RestaurantResource, '/api/restaurants/<int:restaurant_id>')
    api.add_resource(PizzaListResource, '/api/pizzas')
    api.add_resource(RestaurantPizzaResource, '/api/restaurant_pizzas')

    return app
