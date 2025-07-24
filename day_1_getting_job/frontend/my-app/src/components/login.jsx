import React,  { useState } from 'react';
import { useNavigate } from "react-router-dom";

     
import axios from 'axios';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
   const navigate = useNavigate();


  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('username:', username);
    console.log('Password:', password);
    axios.post('http://localhost:3000/signin', { username, password })
      .then(response => {
        setIsLoggedIn(true);
            localStorage.setItem("token", response.data.token);
navigate("/todos");
        console.log('Login successful:', response.data);


      }).catch(error => {
        console.error('Login failed:', error);
        setError('Login failed. Please check your credentials.');

        });

    // Handle login logic here
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>username:</label>
          <input
            type="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
        {isLoggedIn && <p>Login successful!</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default Login;