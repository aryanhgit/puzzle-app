import React from 'react';
import { useForm } from 'react-hook-form';
import { Link } from 'react-router';

const SignUpPage = () => {
    const { register, handleSubmit, formState: { errors } } = useForm();

    const [error, setError] = React.useState(null);

    const onSubmit = (data) => {
        console.log(data);
        if (data.password !== data.confirmPassword) {
            alert("Passwords do not match!");
            return;
        }
        // send the data to your backend API
        fetch('/auth/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // Handle success, e.g., redirect to login page
            })
            .catch((error) => {
                console.error('Error:', error);
                // Handle errors, e.g., display an error message
            });

    };

    return (
        <div className="page-container sign-container">
            <h1>SignUp Page</h1>
            <p>Welcome to the signup page!</p>

            <form onSubmit={handleSubmit(onSubmit)}>
                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input type="text" className="form-control" id="username" placeholder="Enter username"
                        {...register("username", { required: true, minLength: 3 })}
                    />
                    {errors.username && <p className="text-danger">Username is required and must be at least 3 characters.</p>}
                </div>

                <div className="form-group">
                    <label htmlFor="exampleInputEmail1">Email address</label>
                    <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"
                        {...register("email", { required: true, pattern: /^\S+@\S+$/i })}
                    />
                    <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
                    {errors.email && <p className="text-danger">Email is required and must be valid.</p>}
                </div>

                <div className="form-group">
                    <label htmlFor="exampleInputPassword1">Password</label>
                    <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password"
                        {...register("password", { required: true, minLength: 6 })}
                    />
                    {errors.password && <p className="text-danger">Password is required and must be at least 6 characters.</p>}
                </div>

                <div className="form-group">
                    <label htmlFor="confirmPassword">Confirm Password</label>
                    <input type="password" className="form-control" id="confirmPassword" placeholder="Confirm Password"
                        {...register("confirmPassword", { required: true, minLength: 6 })}
                    />
                    {errors.confirmPassword && <p className="text-danger">Confirm Password is required and must be at least 6 characters.</p>}
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
                Already have an account? <Link to="/login">Login</Link>
            </p>

        </div>
    );
}

export default SignUpPage;
