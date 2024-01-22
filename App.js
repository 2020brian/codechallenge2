import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RestaurantList from './components/RestaurantList';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={RestaurantList} />
      </Switch>
    </Router>
  );
};

export default App;
