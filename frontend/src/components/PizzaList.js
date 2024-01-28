import React, { useState, useEffect } from 'react';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    const fetchPizzas = async () => {
      try {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/pizzas`);
        if (!response.ok) {
          throw new Error('Error fetching pizzas');
        }

        const data = await response.json();
        setPizzas(data);
      } catch (error) {
        console.error('Error fetching pizzas:', error.message);
      }
    };

    fetchPizzas();
  }, []);

  return (
    <div>
      <h2>Pizzas</h2>
      <ul>
        {pizzas.map(pizza => (
          <li key={pizza.id}>
            {pizza.name} - {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PizzaList;
