// src/components/RestaurantList.js
import React, { useState, useEffect } from 'react';
import api from '../services/api';

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await api.get('/restaurants');
        setRestaurants(response.data);
      } catch (error) {
        console.error('Error fetching restaurants:', error);
      }
    };

    fetchRestaurants();
  }, []);

  return (
    <div>
      <h2>Restaurant List</h2>
      {/* Render restaurant data */}
    </div>
  );
};

export default RestaurantList;
