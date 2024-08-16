// src/components/Header.js
import React from 'react';

function Header() {
    return (
        <header style={styles.header}>
            <h1 style={styles.title}>Appointment Manager</h1>
            <p style={styles.subtitle}>TO START USING THIS PAGE, YOU MUST</p>
            <button style={styles.loginButton}>LOG IN</button>
        </header>
    );
}

const styles = {
    header: {
        backgroundColor: '#000',
        color: '#fff',
        margin: '-20px',
        padding: '20px',
        textAlign: 'center',
        alignItems: 'center',
        width: '100vw',
        height: '20vw',

        
    },
    title: {
        fontSize: '2rem',
    },
    subtitle: {
        fontSize: '1.2rem',
    },
    loginButton: {
        marginTop: '70px',
        padding: '10px 20px',
        fontSize: '1rem',
        backgroundColor: '#fff',
        color: '#000',
        border: '1px solid #000',
        cursor: 'pointer',
    }
};

export default Header;
