import React, { useState } from 'react';
import { Navigate } from 'react-router-dom';

const Navbar = () => {
  const storedUsername = localStorage.getItem('username');
  const [cerrarSesion, setCerrarSesion] = useState(false);

  const handleCerrarSesionClick = () => {
    // Eliminar el nombre de usuario del almacenamiento local
    localStorage.removeItem('username');
    // Redirigir a la página de inicio después de cerrar sesión
    setCerrarSesion(true);
  };

  if (cerrarSesion) {
    return <Navigate to="/" />;
  }

  return (
    <header className="bg-green-500 text-white py-4">
      <div className="container mx-auto flex items-center justify-between">
        <h1 className="text-2xl font-semibold">WattVisor</h1>

        {storedUsername && (
          <div className="flex items-center">
            <p className="mr-4">Bienvenido, <span>{storedUsername}!</span></p>
            <button
              onClick={handleCerrarSesionClick}
              className='bg-red-500 text-white p-2 rounded-md hover:bg-red-600'
            >
              Cerrar Sesión
            </button>
          </div>
        )}
      </div>
    </header>
  );
};

export default Navbar;
