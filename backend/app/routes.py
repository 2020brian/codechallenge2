# backend/app/routes.py
from flask import jsonify, request
from flask_restful import Api, Resource
from backend.app import create_app, db
from backend.app.models import Restaurant, Pizza, RestaurantPizza

app = create_app()
api = Api(app)

# Define resources
class RestaurantListResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_data = [{
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        } for restaurant in restaurants]
        return jsonify(restaurants_data)

class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            pizzas_data = [{
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            } for pizza in restaurant.pizzas]
            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                'pizzas': pizzas_data
            }
            return jsonify(restaurant_data)
        else:
            return jsonify({'error': 'Restaurant not found'}), 404

    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete(
