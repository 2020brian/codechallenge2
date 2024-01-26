from flask import Blueprint, jsonify, request
from app.models import Restaurant, Pizza, RestaurantPizza, db

# Define blueprints
restaurant_bp = Blueprint('restaurant', __name__)
pizza_bp = Blueprint('pizza', __name__)

# Routes for Restaurant
@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        for restaurant in restaurants
    ])

@restaurant_bp.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": [
                {
                    "id": pizza.id,
                    "name": pizza.name,
                    "ingredients": pizza.ingredients
                }
                for pizza in restaurant.pizzas
            ]
        })
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@restaurant_bp.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        # Delete associated RestaurantPizzas first
        RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404

# Routes for Pizza
@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        for pizza in pizzas
    ])

@pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')

    # Validation
    if not(1 <= price <= 30):
        return jsonify({"errors": ["Validation errors"]}), 400

    restaurant_pizza = RestaurantPizza(
        pizza_id=pizza_id,
        restaurant_id=restaurant_id,
        price=price
    )
    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    })
