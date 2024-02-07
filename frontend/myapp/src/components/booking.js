import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function Booking() {

    const baseURL = "http://localhost:8000/";
    const [services, setServices] = useState([]);
    const [days, setDays] = useState([]);
    const [times, setTimes] = useState([]);
    const [selectedService, setSelectedService] = useState('');
    const [selectedDay, setSelectedDay] = useState('');
    const [selectedTime, setSelectedTime] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get(`${baseURL}/booking/`).then((response) => {
            console.log("Response from backend:", response.data);

            setServices(response.data.services);
            setDays(response.data.days);
            setTimes(response.data.times); // Flatten the array
        })
            .catch((error) => {
                console.error("Error fetching data:", error);
            });
    }, []);
    
    const handleSubmit = (event) => {   
        event.preventDefault();

        axios.post('http://localhost:8000/booking/', {
            service: selectedService,
            day: selectedDay,
            time: selectedTime,
        })
            .then(response => {
                console.log(response);
                setMessage(response.data.message);
                if (response.data.success) {
                    window.location.href = '/';
                    console.log('Everything fine');
                } else {
                    console.log('Appointment has not been created');
                }
            })
            .catch(error => {
                console.error('HandleSubmit error', error   );
            });
    };

    return (
        <div>
            <h1>Reservas</h1>

            {/* Booking Form */}
            <form onSubmit={handleSubmit}>
                {/* Service Dropdown */}
                <label htmlFor="service">Seleccione un servicio:</label>
                <select
                    name="service"
                    id="service"
                    onChange={(e) => setSelectedService(e.target.value)}
                    value={selectedService}
                >
                    <option value="" disabled>
                        Servicio
                    </option>
                    {services.map((service) => (
                        <option key={service} value={service}>{service}</option>
                    ))}
                </select>

                <br />

                {/* Day Dropdown */}
                <label htmlFor="day">Seleccione un dia:</label>
                <select
                    name="day"
                    id="day"
                    value={selectedDay}
                    onChange={(e) => setSelectedDay(e.target.value)}
                >
                    <option value="" disabled>
                        Dia
                    </option>
                    {days.map((day) => (
                        <option key={day} value={day}>{day}</option>
                    ))}
                </select>

                <br />

                {/* Time Dropdown */}
                <label htmlFor="time">Seleccione una hora:</label>
                <select
                    name="time"
                    id="time"
                    value={selectedTime}
                    onChange={(e) => setSelectedTime(e.target.value)}
                >
                    <option value="" disabled>
                        Hora
                    </option>
                    {Array.from(new Set(times)).map((time) => (
                        <option key={time} value={time}>{time}</option>
                    ))}
                </select>

                <br />

            </form>
            <form onClick={handleSubmit}>
                <button type="submit">Submit</button>
            </form>
            <h2>Dias disponibles:</h2>
        </div>
    );
};
