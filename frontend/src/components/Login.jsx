import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';
import { useUser } from './UserContext';
import axios from 'axios';



function Login() {
  const [username, setUsername] = useState('');
  const [loginSuccess, setLoginSuccess] = useState(false);
  const [goSuccess, setGoSuccess] = useState(false);
  const { login } = useUser();
    

     // Estado para manejar los valores de los campos del formulario
  const [credentials, setCredentials] = useState({
    username: '',
    password: '',
  });

  // Función para manejar cambios en los campos de entrada
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials((prevCredentials) => ({
      ...prevCredentials,
      [name]: value,
    }));
  };

  const handleRegisterClick = () => {
    setGoSuccess(true);
  };

  if (goSuccess) {
    return <Navigate to="/register" />;
  }

  // Función para manejar el envío del formulario
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post('http://localhost:8000/api/login/', credentials);

      // Manejar la respuesta del servidor (por ejemplo, mostrar un mensaje de éxito)
      console.log('Respuesta del servidor:', response.data);

      if (response.data.message === 'Inicio de sesión exitoso.') {
        setUsername(credentials.username)
        setLoginSuccess(true);
      } else {
        // Si hay un mensaje de error, puedes manejarlo aquí
        console.error('Error en el inicio de sesión:', response.data.error);
      }
    } catch (error) {
      console.error('Error al enviar credenciales'+ error);
    }

  };

  if (loginSuccess) {
    login(username)
    return <Navigate to="/home" />;
  }



  return (
    <>
    <div className='flex items-center justify-center h-screen'>
      <div className='bg-white p-8 rounded shadow-md w-96'>
          <h1 className='text-2xl font-semibold mb-6'>Login</h1>
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

            <div className='flex space-x-24'>
            <button 
                onClick={handleRegisterClick}
                className='bg-red-500 text-white p-2 rounded-md hover:bg-red-600'>
                Registrarse
            </button>
              <button 
                type='submit'
                className='bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600'>
                Iniciar Sesión
              </button>
            </div>
            
          </form>
        </div>
      </div>

    </>
  )
}

export default Login