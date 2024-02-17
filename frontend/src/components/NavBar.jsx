// En Navbar.js
import React from 'react';

const Navbar = () => {
  const storedUsername = localStorage.getItem('username');
  return (
    <header className="bg-green-500 text-white py-4">
      <div className="container mx-auto ">
        
        <h1 className="text-2xl font-semibold">WattVisor</h1>
        {storedUsername && (
          <p>Bienvenido, <span>{storedUsername}!</span></p>
        )}
        
      </div>
    </header>
  );
};

export default Navbar;
