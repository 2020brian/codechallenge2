const apiUrl = 'http://localhost:5000/api';  // Update with your backend URL

const pizzaApi = {
  getRestaurants: async () => {
    const response = await fetch(`${apiUrl}/restaurants`);
    const data = await response.json();
    return data;
  },

  // Add more functions for other API calls
};

export default pizzaApi;
