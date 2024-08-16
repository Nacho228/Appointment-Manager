// src/App.js
import React from 'react';
import Header from './components/header';
import Services from './components/services';
import Times from './components/times';
import Button from './components/button';
import Appointments from './components/appointments';

function App() {
    return (
        <div style={styles.container}>
            <Header />
            <div style={styles.mainContent}>
                <Services />
                <Times />
            </div>
            <Button text="Book" />
            <Appointments />
        </div>
    );
}

const styles = {
    container: {
        fontFamily: 'Arial, sans-serif',
        maxWidth: '800px',
        margin: '0 auto',
        padding: '20px',
    },
    mainContent: {
        display: 'flex',
        justifyContent: 'space-between',
    }
};

export default App;
