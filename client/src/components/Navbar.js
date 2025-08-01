import React from 'react';
import { Link } from 'react-router';

const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <Link className="navbar-brand" to="/">Posts</Link>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item active">
                        <Link className="nav-link active" to="/">Home</Link>
                    </li>
                    <li className="nav-item active">
                        <Link className="nav-link active" to="/create_post">Create posts</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link active" to="/signup">Sign Up</Link >
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link active" to="/login">Login</Link >
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link active">Log out</Link >
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
