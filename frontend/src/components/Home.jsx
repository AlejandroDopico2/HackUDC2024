import React, { useState, useEffect } from 'react'
import { Navigate, useNavigate } from 'react-router-dom';
import UploadModal from './UploadModal';
import UploadModalPdf from './UploadModalPdf';

const Home = () => {
    const [modalOpen, setModalOpen] = useState(false);
    const [modalOpenPdf, setModalOpenPdf] = useState(false);
    const [goGraficas, setGoGraficas] = useState(false);

    const navigate = useNavigate();

    useEffect(() => {
      // Verificar si el usuario está logueado al cargar el componente
      const isLoggedIn = localStorage.getItem('username');

      if (!isLoggedIn) {
        // Si no está logueado, redireccionar a la página de inicio de sesión
        navigate('/');
      }
    }, [navigate]);

    const openModal = () => {
      setModalOpen(true);
    };
  
    const closeModal = () => {
      setModalOpen(false);
    };

    const openModalPdf = () => {
      setModalOpenPdf(true);
    };
  
    const closeModalPdf = () => {
      setModalOpenPdf(false);
    };

    const handleGraficasClick = () => {
      setGoGraficas(true)
    };


    if (goGraficas) {
      return <Navigate to="/gastos" />;
    }

    return (
      <>
        <div 
        className='m-5 p-5 flex border rounded-md'
        >
          <button 
            className='focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"'
            onClick={openModal}
          >upload</button>
          <button 
            className='focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"'
            onClick={handleGraficasClick}
          >graficas</button>
          <button 
            className='focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"'
            onClick={openModalPdf}
          >Facturas</button>

          {/* <button 
            className='focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"'
            onClick={activarFactura}
          >Mostrar Factura</button> */}
        </div>
        {modalOpen && <UploadModal closeModal={closeModal} />}
        {modalOpenPdf && <UploadModalPdf closeModalPdf={closeModalPdf}/>}

      </>
    )
}

export default Home