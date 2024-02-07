// Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { useState, useEffect } from 'react';

export default function HomePage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');

  useEffect(() => {
    async function checkAuthentication() {
      try {
        const response = await axios.get('http://localhost:8000/check-authentication/');
        if (response.data.authenticated) {
          setIsLoggedIn(true);
          setUsername(response.data.username);
        }
      } catch (error) {
        setIsLoggedIn(false);
        setUsername('');
      }
    }
    checkAuthentication();
  }, []);

  return (
    <div>
      {isLoggedIn ? (
        <div>
          <h1>Welcome, {username}!</h1>
          <p>This is your home page. Feel free to explore!</p>
          <Link to="/booking"><button>Make an appointment</button></Link>
          <Link to="/show_appointments"><button>Show Appointments</button></Link>
        </div>
      ) : (
        <div>
          <h1>Welcome, Guest!</h1>
          <Link to="/register"><button>Register</button></Link>
        </div>
      )}
    </div>
  );
}