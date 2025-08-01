import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect } from 'react';
import './styles/main.css';
import ReactDOM from 'react-dom/client';
import Navbar from './components/Navbar';
import { BrowserRouter, Routes, Route } from "react-router";
import HomePage from './components/Home';
import SignUpPage from './components/SignUp';
import LoginPage from './components/Login';
import CreatePostPage from './components/CreatePost';

const App = () => {
    return (
        <BrowserRouter>
            <div className='container'>
                <Navbar />
                <Routes> 
                    <Route path='/' element={<HomePage />} />
                    <Route path='/signup' element={<SignUpPage />} />
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='create_post' element={<CreatePostPage />} />
                </Routes> 
            </div>
        </BrowserRouter>
    )
}

const root = document.getElementById("root");

ReactDOM.createRoot(root).render(
    <App />
);