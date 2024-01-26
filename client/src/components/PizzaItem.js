import React from 'react';

const PizzaItem = ({ pizza }) => {
  

  return (
    <div className="pizza-item">
      <h2>{pizza.name}</h2>
      <p>{pizza.description}</p>
      <p>Price: ${pizza.price}</p>
      {}
    </div>
  );
};

export default PizzaItem;
