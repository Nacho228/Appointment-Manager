import React, { useEffect } from 'react';
import axios from 'axios';


function ShowAppointment() {
    const baseURL = "http://localhost:8000/";

    useEffect(() => {
        axios.get(`${baseURL}/my_appointments/`).then((response) => {
            console.log("Response from backend:", response.data);
        })
    })
    
  return (
    <div>
      <h2>Welcome User</h2>
      <p>This is your appointment page. Here are yours appointments!</p>
    </div>
  );
}

export default ShowAppointment;
