// Gastos.js
import React, {useState, useEffect} from 'react';
import ColumnChart from './ColumnChart';
import LineChart from './LineChart';
import { Navigate, useNavigate } from 'react-router-dom';
import Home from './Home';
import axios from 'axios';

function Gastos() {
    const storedUsername = localStorage.getItem('username');
    const [goSuccess, setGoSuccess] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
      // Verificar si el usuario está logueado al cargar el componente
      const isLoggedIn = localStorage.getItem('username');

      if (!isLoggedIn) {
        // Si no está logueado, redireccionar a la página de inicio de sesión
        navigate('/');
      }
    }, [navigate]);

    const handleVolverClick = () => {
        setGoSuccess(true);
    };
    const handleLlamadaClick = async () => {
      try {
         await axios.post(`http://localhost:8000/api/predict/${storedUsername}/`, storedUsername, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
  
  
      } catch (error) {
        console.error('Error al enviar credenciales'+ error);
      }
    };

    if (goSuccess) {
        return <Navigate to="/home" />;
    }
  return (
    <div className='p-5'>
        <button 
            onClick={handleVolverClick}
            className='bg-red-500 text-white p-2 rounded-md hover:bg-red-600'>
            Volver
        </button>
        <button 
            onClick={handleLlamadaClick}
            className='bg-red-500 text-white p-2 rounded-md hover:bg-blue-600'>
            Predict
        </button>
      <div className='text-center mb-5'>
        <h1 className='text-3xl text-green-500'>Gastos</h1>
      </div>

      <div className='flex items-center justify-center w-3/4'>
        <ColumnChart />
      </div>

      {/* <div className='flex items-center justify-center'>
          <LineChart />
      </div> */}
    </div>
  );
}

export default Gastos;