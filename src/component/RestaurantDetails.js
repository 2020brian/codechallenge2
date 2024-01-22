import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

const RestaurantDetails = () => {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    const fetchRestaurantDetails = async () => {
      try {
        const response = await api.get(`/restaurants/${id}`);
        setRestaurant(response.data);
      } catch (error) {
        console.error('Error fetching restaurant details:', error);
      }
    };

    fetchRestaurantDetails();
  }, [id]);

  if (!restaurant) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{restaurant.name}</h2>
      <p>{restaurant.address}</p>
      <h3>Pizzas</h3>
      <ul>
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong>
            <p>{pizza.ingredients}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantDetails;
