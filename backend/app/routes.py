# backend/app/routes.py

from flask import jsonify, request
from backend.app import app, db
from backend.app.models import Restaurant, Pizza, RestaurantPizza
from backend import create_app

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        return jsonify([restaurant.serialize() for restaurant in restaurants])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['GET', 'DELETE'])
def restaurant_details(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    if request.method == 'GET':
        return jsonify(restaurant.serialize())

    elif request.method == 'DELETE':
        try:
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    try:
        pizzas = Pizza.query.all()
        return jsonify([pizza.serialize() for pizza in pizzas])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()

        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        # Validate data
        if price < 1 or price > 30:
            return jsonify({"errors": ["Validation error: Price must be between 1 and 30"]}), 400

        # Check if pizza and restaurant exist
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not pizza or not restaurant:
            return jsonify({"errors": ["Validation error: Invalid pizza or restaurant ID"]}), 400

        # Create new RestaurantPizza
        restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify(pizza.serialize()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
