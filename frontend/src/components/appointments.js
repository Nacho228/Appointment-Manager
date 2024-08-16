// src/components/Appointments.js
import React from 'react';

function Appointments() {
    return (
        <button style={styles.button}>My appointments</button>
    );
}

const styles = {
    button: {
        padding: '10px 20px',
        fontSize: '1rem',
        backgroundColor: '#000',
        color: '#fff',
        border: '1px solid #000',
        cursor: 'pointer',
        float: 'right',
        marginTop: '20px',
    }
};

export default Appointments;
