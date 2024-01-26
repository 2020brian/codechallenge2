import React from 'react';
import './App.css';
import PizzaList from './components/PizzaList';
import RestaurantList from './components/RestaurantList';
import RestaurantDetail from './components/RestaurantDetail';

function App() {
  return (
    <div className="App">
      <h1>Pizza Restaurant App</h1>
      <PizzaList />
      <hr />
      <RestaurantList />
      <hr />
      <RestaurantDetail />
    </div>
  );
}

export default App;
