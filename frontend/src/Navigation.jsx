// src/Navigation.jsx

import React from 'react';
import { Link } from 'react-router-dom';

function Navigation() {
  return (
    <nav>
      <ul>
        <li><Link to="/">Inicio</Link></li>
        <li><Link to="/Register">Acerca de</Link></li>
        <li><Link to="/Login">Contacto</Link></li>
      </ul>
    </nav>
  );
}

export default Navigation;
