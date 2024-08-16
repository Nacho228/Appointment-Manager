// src/components/Button.js
import React from 'react';

function Button({ text }) {
    return (
        <button style={styles.button}>{text}</button>
    );
}

const styles = {
    button: {
        padding: '10px 20px',
        fontSize: '1rem',
        backgroundColor: '#fff',
        color: '#000',
        border: '1px solid #000',
        cursor: 'pointer',
        margin: '20px 0',
    }
};

export default Button;
