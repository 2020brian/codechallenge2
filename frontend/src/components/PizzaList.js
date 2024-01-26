import React, { useState, useEffect } from 'react';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    // Fetch pizzas from your Flask backend
    // Update 'REACT_APP_API_URL' with the actual environment variable name on Render
    fetch(`${process.env.REACT_APP_API_URL}/pizzas`)
      .then(response => response.json())
      .then(data => setPizzas(data));
  }, []);

  return (
    <div>
      <h2>Pizza List</h2>
      <ul>
        {pizzas.map(pizza => (
          <li key={pizza.id}>{pizza.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default PizzaList;
