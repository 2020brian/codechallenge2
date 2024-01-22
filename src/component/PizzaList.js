import React, { useState, useEffect } from 'react';
import api from '../services/api';

const PizzaList = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    const fetchPizzas = async () => {
      try {
        const response = await api.get('/pizzas');
        setPizzas(response.data);
      } catch (error) {
        console.error('Error fetching pizzas:', error);
      }
    };

    fetchPizzas();
  }, []);

  return (
    <div>
      <h2>Pizza List</h2>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong>
            <p>{pizza.ingredients}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PizzaList;
