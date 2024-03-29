import React, { useState, useEffect } from 'react';
import ColumnChart from './ColumnChart';
import { Navigate, useNavigate } from 'react-router-dom';
import Home from './Home';
import axios from 'axios';

function Gastos() {
    const storedUsername = localStorage.getItem('username');
    const [goSuccess, setGoSuccess] = useState(false);
    const [tiempo, setTiempo] = useState('mes'); // Estado para guardar el valor seleccionado del primer select
    const [anho, setAnho] = useState(2023); // Estado para guardar el valor seleccionado del primer select

    const navigate = useNavigate();

    useEffect(() => {
      // Verificar si el usuario está logueado al cargar el componente
      const isLoggedIn = localStorage.getItem('username');

      if (!isLoggedIn) {
        // Si no está logueado, redireccionar a la página de inicio de sesión
        navigate('/');
      }
    }, [navigate]);

    useEffect( ()=>{
      console.log(tiempo)
      const param = {
        username : storedUsername,
        time : tiempo,
        year : anho,
      };

      if("mes" === tiempo){
        
      }

      // try {
        
      //   const response = await axios.get('http://localhost:8000/api/columnChart/', { param });
      //   return response.data;
      // } catch (error) {
      //   console.error("Error al realizar la petición GET de las gráficas: " + error);
      //   return [];
      // }

      //peticion de los años/meses/dias
    },[tiempo])

    const handleVolverClick = () => {
        setGoSuccess(true);
    };

    const handleTiempoChange = (event) => {
        setTiempo(event.target.value); // Actualizar el estado 'tiempo' con el valor seleccionado del primer select
        
    };

    const handleAnhoChange = (event) => {
      setAnho(event.target.value); // Actualizar el estado 'tiempo' con el valor seleccionado del primer select
      
    };

    const handleLlamadaClick = async () => {
      try {
         await axios.post(`http://localhost:8000/api/predict/${storedUsername}/`, storedUsername, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
  
  
      } catch (error) {
        console.error('Error al enviar credenciales' + error);
      }
    };

    if (goSuccess) {
        return <Navigate to="/home" />;
    }


    return (
        <div className='p-5'>
            <button 
              onClick={handleVolverClick}
              className='m-10 bg-red-500 text-white p-3 rounded-lg hover:bg-red-600'>
              Volver
            </button>
            <button 
              onClick={handleLlamadaClick}
              className='bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600'>
              Predict
            </button>

            <div className='text-center mb-5'>
                <h1 className='text-3xl text-green-500'>Gastos</h1>
            </div>

            <div className='flex items-center justify-center mb-10'>
              {/* Contenedor de los selects */}
              <div className='flex items-center p-2 bg-gray-100 rounded-md shadow-md'>
                {/* Primer select */}
                  <select
                    value={tiempo}
                    onChange={handleTiempoChange}
                    className='w-30 p-2 border border-gray-300 rounded-md shadow-md focus:outline-none focus:border-blue-500'
                  >
                    <option value='anho'>Año</option>
                    <option value='mes'>Mes</option>
                    <option value='dia'>Dia</option>
                  </select>

                {/* Espacio entre los selects */}
                <div className='mx-4'></div>

                {/* Segundo select */}
                  <select
                    value={anho}
                    onChange={handleAnhoChange}
                    className='w-30 p-2 border border-gray-300 rounded-md shadow-md focus:outline-none focus:border-blue-500'
                  >
                  </select>
              </div>
            </div>

            <div className='flex items-center justify-center w-3/4 p-2 bg-gray-100 rounded-md shadow-md'>
                <ColumnChart />
            </div>
        </div>
    );
}

export default Gastos;
