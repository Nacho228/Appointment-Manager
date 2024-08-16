// src/components/Times.js
import React from 'react';

function Times() {
    const times = ["03:00 PM", "03:00 PM", "03:00 PM", "03:00 PM", "03:00 PM", "03:00 PM"];

    return (
        <div style={styles.container}>
            <h2 style={styles.title}>Available Start Times</h2>
            <div style={styles.grid}>
                {times.map((time, index) => (
                    <div key={index} style={styles.timeBox}>{time}</div>
                ))}
            </div>
        </div>
    );
}

const styles = {
    container: {
        padding: '20px',
        textAlign: 'left',
    },
    title: {
        fontSize: '1.5rem',
        marginBottom: '10px',
    },
    grid: {
        display: 'grid',
        gridTemplateColumns: 'repeat(2, 1fr)',
        gap: '10px',
    },
    timeBox: {
        padding: '10px',
        backgroundColor: '#000',
        color: '#fff',
        textAlign: 'center',
    }
};

export default Times;
