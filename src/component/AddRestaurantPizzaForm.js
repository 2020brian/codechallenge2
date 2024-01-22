import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import api from '../services/api';

const AddRestaurantPizzaForm = () => {
  const [price, setPrice] = useState('');
  const [pizzaId, setPizzaId] = useState('');
  const [restaurantId, setRestaurantId] = useState('');
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('/restaurant_pizzas', {
        price: parseFloat(price),
        pizza_id: parseInt(pizzaId, 10),
        restaurant_id: parseInt(restaurantId, 10),
      });

      console.log('Added RestaurantPizza:', response.data);
      history.push('/'); // Redirect to home after successful submission
    } catch (error) {
      console.error('Error adding RestaurantPizza:', error);
    }
  };

  return (
    <div>
      <h2>Add Restaurant Pizza</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Price:
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>
        <label>
          Pizza ID:
          <input type="number" value={pizzaId} onChange={(e) => setPizzaId(e.target.value)} />
        </label>
        <label>
          Restaurant ID:
          <input type="number" value={restaurantId} onChange={(e) => setRestaurantId(e.target.value)} />
        </label>
        <button type="submit">Add Restaurant Pizza</button>
      </form>
    </div>
  );
};

export default AddRestaurantPizzaForm;
