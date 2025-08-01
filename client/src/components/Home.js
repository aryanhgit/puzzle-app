import React from 'react';
import { Link } from 'react-router';

const HomePage = () => {
    return (
        <div className="page-container home-container">
            <h1 className='header'>Home Page</h1>
            <p>Welcome to the home page!</p>
            <Link to="/create_post" className='btn btn-primary btn-lg'>Get Started</Link>
        </div>
    );  
}

export default HomePage;
