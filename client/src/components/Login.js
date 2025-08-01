import React from 'react';
import { useForm } from 'react-hook-form';
import { Link } from 'react-router';

const LoginPage = () => {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const onSubmit = (data) => {
        console.log(data);
        // send the data to your backend API
        // fetch('http://localhost:5000/signup', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify(data),
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log('Success:', data);
        //     // Handle success, e.g., redirect to login page
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        //     // Handle errors, e.g., display an error message
        // });

    };

    return (
        <div className="page-container login-container">
            <h1>Login Page</h1>

            <form onSubmit={handleSubmit(onSubmit)}>
                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input type="text" className="form-control" id="username" placeholder="Enter username"
                        {...register("username", { required: true, minLength: 3 })}
                    />
                    {errors.username && <p className="text-danger">Username is required and must be at least 3 characters.</p>}
                </div>

                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input type="password" className="form-control" id="password" placeholder="Password"
                        {...register("password", { required: true, minLength: 6 })}
                    />
                    {errors.password && <p className="text-danger">Password is required and must be at least 6 characters.</p>}
                </div>
                
                <div className="form-group form-check">
                    <input type="checkbox" className="form-check-input" id="exampleCheck1"
                        {...register("rememberMe")}
                    />
                    <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
            
            <p className="mt-3">
                Don't have an account? <Link to="/signup">Sign Up</Link>
            </p>
            
        </div>
    );
}

export default LoginPage;
