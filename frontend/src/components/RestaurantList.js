import React, { useState, useEffect } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/restaurants`);
        if (!response.ok) {
          throw new Error('Error fetching restaurants');
        }

        const data = await response.json();
        setRestaurants(data);
      } catch (error) {
        console.error('Error fetching restaurants:', error.message);
      }
    };

    fetchRestaurants();
  }, []);

  return (
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            {restaurant.name} - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;
