import React, { useState, useEffect } from 'react';
import pizzaApi from '../services/pizzaApi';

const Menu = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      const data = await pizzaApi.getRestaurants();
      setRestaurants(data);
    };

    fetchRestaurants();
  }, []);

  return (
    <div>
      <h2>Menu</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <strong>{restaurant.name}</strong> - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Menu;
