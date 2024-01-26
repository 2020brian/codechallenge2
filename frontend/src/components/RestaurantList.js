import React, { useState, useEffect } from 'react';

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch restaurants from your Flask backend
    // Update 'REACT_APP_API_URL' with the actual environment variable name on Render
    fetch(`${process.env.REACT_APP_API_URL}/restaurants`)
      .then(response => response.json())
      .then(data => setRestaurants(data));
  }, []);

  return (
    <div>
      <h2>Restaurant List</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>{restaurant.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantList;
