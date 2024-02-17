import React, { useState } from 'react'


function Login() {

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

  // Función para manejar el envío del formulario
  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Aquí puedes agregar lógica para enviar las credenciales al servidor
    // por ejemplo, usando una solicitud HTTP con fetch o axios.

    // En este ejemplo, simplemente mostramos las credenciales en la consola.
    console.log('Credenciales enviadas:', credentials);
  };

  return (
    <>
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

          {/* Botón de enviar */}
          <button 
            type='submit'
            className='bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600'>
            Iniciar Sesión
          </button>
        </form>
      </div>
    </>
  )
}

export default Login