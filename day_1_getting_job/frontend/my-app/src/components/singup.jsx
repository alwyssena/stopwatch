import { useState } from "react";

import axios from "axios";

const Signup= () => {   
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const [error, setError] = useState(null);
    const [isSignedUp, setIsSignedUp] = useState(false);


const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Username:', username);
        console.log('Email:', email);
        console.log('Password:', password);
        console.log('Confirm Password:', confirmPassword);
        if (password !== confirmPassword) {
            setError('Passwords do not match.');
            return;
        }
        axios.post('http://localhost:3000/signup', { username, email, password,confirmPassword})
            .then(response => {
                setIsSignedUp(true);
                console.log('Signup successful:', response.data);
            })
            .catch(error => {
                console.error('Signup failed:', error);
                setError('Signup failed. Please try again.');
            });

    };

    return (

        <div>
        <h1>Signup Page</h1>
        <form onSubmit={handleSubmit}>
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" name="username" required value={username} onChange={(e) => setUsername(e.target.value)} />

            <label htmlFor="email">Email:</label>
            <input type="email" id="email" name="email" required value={email} onChange={(e) => setEmail(e.target.value)} />

            <label htmlFor="password">Password:</label>
            <input type="password" id="password" name="password" required value={password} onChange={(e) => setPassword(e.target.value)} />

            <label htmlFor="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" name="confirmPassword" required value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />

            <button type="submit">Sign Up</button>
        </form>
        {isSignedUp && <p>Signup successful!</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <p>Already have an account? <a href="/login">Login here</a></p>

        </div>
    );
    }
export default Signup;