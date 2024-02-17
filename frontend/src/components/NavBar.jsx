// En Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import { useUser } from './UserContext';

const Navbar = () => {
    const { username } = useUser();
  return (
    <header className="bg-green-500 text-white py-4">
      <div className="container mx-auto ">
        
        <h1 className="text-2xl font-semibold">WattVisor</h1>
        {username && (
          <p>Bienvenido, <span>{username}!</span></p>
        )}
        
      </div>
    </header>
  );
};

export default Navbar;
