import axios from 'axios';

// Replace with your actual API endpoint
const API_URL = '/auth';

const login = async (username, password) => {
    try {
        const response = await axios.post(`${API_URL}/login`, {
            username,
            password,
        });

        if (response.data.token) {
            // Store the token in local storage
            localStorage.setItem('user_token', response.data.token);
        }
        return response.data;
    } catch (error) {
        throw error;
    }
};

const logout = () => {
    // Remove the token from local storage
    localStorage.removeItem('user_token');
};

const getCurrentUserToken = () => {
    // Retrieve the token from local storage
    return localStorage.getItem('user_token');
};


const authService = {
    login,
    logout,
    getCurrentUserToken,
};

export default authService;