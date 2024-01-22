// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RestaurantList from './components/RestaurantList';
import RestaurantDetails from './components/RestaurantDetails';
import PizzaList from './components/PizzaList';
import AddRestaurantPizzaForm from './components/AddRestaurantPizzaForm';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={RestaurantList} />
        <Route path="/restaurants/:id" component={RestaurantDetails} />
        <Route path="/pizzas" component={PizzaList} />
        <Route path="/add-pizza" component={AddRestaurantPizzaForm} />
      </Switch>
    </Router>
  );
};

export default App;
