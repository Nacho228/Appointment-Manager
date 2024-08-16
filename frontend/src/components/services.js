import React from 'react';

function Services() {
    const services = ["Doctor care", "Nursing Care", "Medical social services", "Basic assistance care"];

    return (
        <div style={styles.container}>
            <h2 style={styles.title}>Services</h2>
            <ul style={styles.list}>
                {services.map((service, index) => (
                    <li key={index} style={styles.item}>{service}</li>
                ))}
            </ul>
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
    list: {
        listStyleType: 'none',
        padding: 0,
    },
    item: {
        marginBottom: '10px',
        fontSize: '1.2rem',
    }
};

export default Services;
