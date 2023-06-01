import React, { useState } from 'react';
import axios from 'axios';

const PriceRangeForm = () => {
  const [lowerPrice, setLowerPrice] = useState('');
  const [upperPrice, setUpperPrice] = useState('');
  const [laptops, setLaptops] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.get(`http://127.0.0.1:8000/laptopinrange/${lowerPrice}/${upperPrice}/`);
      setLaptops(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  console.log(laptops);
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Lower Price:
          <input type="number" value={lowerPrice} onChange={(e) => setLowerPrice(e.target.value)} />
        </label>
        <label>
          Upper Price:
          <input type="number" value={upperPrice} onChange={(e) => setUpperPrice(e.target.value)} />
        </label>
        <button type="submit">Search</button>
      </form>
      
      <h2>Laptops:</h2>
      {laptops.length === 0 ? (
        <p>No laptops found within the specified price range.</p>
      ) : (
        <ul>
          {laptops.map((laptop) => (
            <li key={laptop.id}>
              <p>Name: {laptop.name}</p>
              <p>Price: {laptop.price}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default PriceRangeForm;