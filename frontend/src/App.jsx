import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import axios from 'axios';

import './components/Header'
import Register from './components/Register'
import Login from './components/Login';
import Home from './components/Home';
import Default from './components/Default';
import Gastos from './components/Gastos';
import Navbar from './components/NavBar';

function App() {
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState('');


  return (
    <div>
      <Navbar/>
      {/* <Navigation /> */}
      <Routes>
        <Route path="/" element={<Default />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
        <Route path="/gastos" element={<Gastos />} />


      </Routes>
      
    </div>
  );
}

export default App
