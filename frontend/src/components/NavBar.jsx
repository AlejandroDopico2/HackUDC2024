// En Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <header className="bg-green-500 text-white py-4">
      <div className="container mx-auto ">
        {/* Contenido de tu encabezado */}
        <h1 className="text-2xl font-semibold">WattVisor</h1>
        {/* Otros elementos del encabezado */}
      </div>
    </header>
  );
};

export default Navbar;
