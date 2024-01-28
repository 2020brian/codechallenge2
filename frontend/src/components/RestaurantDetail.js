import React, { useState, useEffect } from 'react';

function RestaurantDetail() {
  const [restaurant, setRestaurant] = useState(null);

  // Assuming you pass the restaurant ID as a prop
  const restaurantId = 1; // Replace with the actual restaurant ID

  useEffect(() => {
    // Fetch restaurant details from your Flask backend
    // Update 'REACT_APP_API_URL' with the actual environment variable name on Render
    fetch(`${process.env.REACT_APP_API_URL}/restaurants/${restaurantId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error fetching restaurant details');
        }
        return response.json();
      })
      .then(data => setRestaurant(data))
      .catch(error => console.error('Error fetching restaurant details:', error.message));
  }, [restaurantId]);

  return (
    <div>
      <h2>Restaurant Detail</h2>
      {restaurant ? (
        <div>
          <h3>{restaurant.name}</h3>
          <p>Address: {restaurant.address}</p>
          <h4>Pizzas:</h4>
          <ul>
            {restaurant.pizzas.map(pizza => (
              <li key={pizza.id}>
                {pizza.name} - {pizza.ingredients}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>Loading restaurant details...</p>
      )}
    </div>
  );
}

export default RestaurantDetail;
