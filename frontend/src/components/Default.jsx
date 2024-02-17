import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';



function Default() {
    const [goSuccess, setGoSuccess] = useState(false);

    const handleLoginClick = () => {
      setGoSuccess(true);
    };
  
    if (goSuccess) {
      return <Navigate to="/login" />;
    }

  return (
    <>
    <div 
    className='mt-5'>
        <button
            className='bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600'
            onClick={handleLoginClick}
        >Login</button>
    </div>
    <div className='flex items-center justify-center h-screen'>
      <div className='container bg-white p-8 rounded shadow-md flex'>
        <div className='flex-1'>
          <h1 className='text-green-500 text-3xl'>Os presentamos WattVisor</h1>
          <p>Un proyecto creado en una hackathon por</p>
          <ul className="list-none p-0">
            <li className="mb-4">
              <span className="font-bold">Antón Canzobre</span>
            </li>
            <li className="mb-4">
              <span className="font-bold">Alejandro Dopico</span>
            </li>
            <li className="mb-4">
              <span className="font-bold">Abel Juncal</span>
            </li>
            <li>
              <span className="font-bold">Alejandro Garcia</span>
            </li>
          </ul>
        </div>
        <div className='flex-shrink-0 ml-4'>
            <img src="/assets/Logotipo-Gradiant-texto.png" alt="Descripción de la imagen" className="rounded-md" />
        </div>
      </div>
    </div>
  </>
  )
}

export default Default