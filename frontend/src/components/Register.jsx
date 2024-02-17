import React, { useState, useEffect } from 'react'
import { Navigate, useNavigate } from 'react-router-dom';

import axios from 'axios';

function Register() {

     // Estado para manejar los valores de los campos del formulario
  const [credentials, setCredentials] = useState({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    password: '',
  });
  const [goSuccess, setGoSuccess] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
      // Verificar si el usuario está logueado al cargar el componente
      const isLoggedIn = localStorage.getItem('username');

      if (isLoggedIn) {
        // Si no está logueado, redireccionar a la página de inicio de sesión
        navigate('/home');
      }
    }, [navigate]);


  // Función para manejar cambios en los campos de entrada
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prevCredentials) => ({
      ...prevCredentials,
      [name]: value,
    }));
  };

  // Función para manejar el envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Enviar los datos al servidor Django
      const response = await axios.post('http://localhost:8000/api/register/', credentials);

      // Manejar la respuesta del servidor (por ejemplo, mostrar un mensaje de éxito)
      console.log('Respuesta del servidor:', response.data);

    } catch (error) {
      // Manejar errores (por ejemplo, mostrar un mensaje de error)
      console.error('Error al enviar datos al servidor:', error);
    }
  };

  const handleVolverClick = () => {
    setGoSuccess(true);
  };

  if (goSuccess) {
    return <Navigate to="/login" />;
  }

  return (
    <>
    <div className='flex items-center justify-center h-screen'>
    <div className='bg-white p-8 rounded shadow-md w-96'>
        <h1 className='text-2xl font-semibold mb-6'>Register</h1>
        <form onSubmit={handleSubmit}>
          <div className='mb-4'>
            <label htmlFor='username' className='block text-sm font-medium text-gray-600'>
              Username:
            </label>
            <input type='text' 
                id='username' 
                name='username' 
                value={credentials.username}
                onChange={handleInputChange}
                className='mt-1 p-2 w-full border rounded-md' 
                />
          </div>

          <div className='mb-4'>
            <label htmlFor='email' className='block text-sm font-medium text-gray-600'>
              Email:
            </label>
            <input type='email' 
                id='email' 
                name='email' 
                value={credentials.email}
                onChange={handleInputChange}
                className='mt-1 p-2 w-full border rounded-md' 
                />
          </div>

          <div className='mb-4'>
            <label htmlFor='first_name' className='block text-sm font-medium text-gray-600'>
              Name:
            </label>
            <input type='text' 
                id='first_name' 
                name='first_name' 
                value={credentials.first_name}
                onChange={handleInputChange}
                className='mt-1 p-2 w-full border rounded-md' 
                />
          </div>

          <div className='mb-4'>
            <label htmlFor='last_name' className='block text-sm font-medium text-gray-600'>
              Last Name:
            </label>
            <input type='text' 
                id='last_name' 
                name='last_name' 
                value={credentials.last_name}
                onChange={handleInputChange}
                className='mt-1 p-2 w-full border rounded-md' 
                />
          </div>

          <div className='mb-4'>
            <label htmlFor='password' className='block text-sm font-medium text-gray-600'>
              Password:
            </label>
            <input type='password'
                id='password'
                name='password'
                value={credentials.password}
                onChange={handleInputChange}
                className='mt-1 p-2 w-full border rounded-md'/>
          </div>

          <div className='flex space-x-44'>
            <button 
                  onClick={handleVolverClick}
                  className='bg-red-500 text-white p-2 rounded-md hover:bg-red-600'>
                  volver
            </button>
            <button 
              type='submit'
              className='bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600'>
              Register
            </button>
            </div>
          
        </form>
      </div>
      </div>
    </>
  )
}

export default Register