import React, { useState } from 'react';
import axios from 'axios';

export default function Register() {
    const [formData, setFormData] = useState({
        username: '',
        password1: '',
        password2: ''
    });
    const [errors, setErrors] = useState({});
    const [successMessage, setSuccessMessage] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://localhost:8000/register/', formData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });

            if (response.status === 200 && response.data.success) {
                setSuccessMessage(response.data.message);
                setErrors({});
                window.location.href = '/';
            }
            else {
                setErrors(response.data.errors || { message: response.data.message });
            }
        } catch (error) {
            if (error.response) {
                setErrors(error.response.data.errors || { message: error.response.data.message });
            } else {
                console.error('Error:', error.message);
            }
        }
    };

    return (
        <div>
            <h2>Register</h2>
            {successMessage && <div>{successMessage}</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        name="password1"
                        value={formData.password1}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Confirm Password:</label>
                    <input
                        type="password"
                        name="password2"
                        value={formData.password2}
                        onChange={handleChange}
                        required
                    />
                </div>
                {errors && (
                    <div style={{ color: 'red' }}>
                        {Object.values(errors).map((error, index) => (
                            <div key={index}>{error}</div>
                        ))}
                    </div>
                )}
                <button type="submit">Register</button>
            </form>
        </div>
    );
}
