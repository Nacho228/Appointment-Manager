import React from 'react';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './components/Home';
import Booking from './components/booking';
import ShowAppointment from './components/show_appointments';
import Register from './components/register';

function App() {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/booking/' element={<Booking />} />
                <Route path='/show_appointments' element={<ShowAppointment />}></Route>
                <Route path='/register' element={<Register />}></Route>
            </Routes>
        </Router>
    );
}

export default App;

// function home() {
//   return (
//     <Router>
//       <div>
//         <h1>Welcome User</h1>
//       <Link to="/booking"><button>Make an appointment</button></Link>
//       <Route path='/booking' component={booking}></Route>
//       </div>
//     </Router>
//   )
// }
// export default home;
