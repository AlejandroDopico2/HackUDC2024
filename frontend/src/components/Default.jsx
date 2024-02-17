import React, { useState } from 'react'
import { Navigate } from 'react-router-dom';
import logo from '/public/logo2.png'



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
            className='bg-blue-500 text-white p-5 text-xl rounded-md hover:bg-blue-600'
            onClick={handleLoginClick}
        >Login</button>
    </div>
    <div className='flex items-center justify-center h-1/3'>
      <div className='container bg-white p-8 rounded shadow-md flex'>
        <div className='flex-1'>
          <h1 className='text-green-500 text-3xl'>Os presentamos WattVisor</h1>
          <p>Un proyecto creado en una hackathon por</p>
          <ul className="list-none p-0">
            <li className="mb-4">
              <span className="font-bold">Antón Canzobre:</span> 
              <a href="https://www.linkedin.com/in/anton-canzobre-mart%C3%ADnez-ba549a267/" target="_blank" rel="noopener noreferrer" className="text-blue-500 ml-2 underline hover:text-blue-700">LinkedIn</a>
            </li>
            <li className="mb-4">
              <span className="font-bold">Alejandro Dopico:</span>
              <a href="https://www.linkedin.com/in/alejandrodopicocastro/" target="_blank" rel="noopener noreferrer" className="text-blue-500 ml-2 underline hover:text-blue-700">LinkedIn</a>
            </li>
            <li className="mb-4">
              <span className="font-bold">Abel Juncal:</span>
              <a href="https://www.linkedin.com/in/abel-juncal-su%C3%A1rez-52b86a240/" target="_blank" rel="noopener noreferrer" className="text-blue-500 ml-2 underline hover:text-blue-700">LinkedIn</a>
            </li>
            <li>
              <span className="font-bold">Alejandro Garcia:</span>
              <a href="https://www.linkedin.com/in/alejandrogarciagarcia1/" target="_blank" rel="noopener noreferrer" className="text-blue-500 ml-2 underline hover:text-blue-700">LinkedIn</a>
            </li>
          </ul>
        </div>
        <div className='flex-shrink-0 ml-4'>
          <img src={logo} alt="Logo de Gradiant" className='w-64 h-64 mr-2'/>
        </div>
      </div>
    </div>
  </>
  )
}

export default Default