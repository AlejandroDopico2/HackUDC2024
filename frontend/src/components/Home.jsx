import React, { useState } from 'react'
import Navbar from './NavBar'
import UploadModal from './UploadModal';
import { useUser } from './UserContext';

const Home = () => {
    const { username } = useUser();
    const [modalOpen, setModalOpen] = useState(false);

    const openModal = () => {
      setModalOpen(true);
    };
  
    const closeModal = () => {
      setModalOpen(false);
    };
    return (
      <>
        <div 
        className='m-5 p-5 flex border rounded-md'
        >
            <button 
        className='focus:outline-none text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800"'
        onClick={openModal}
        >upload</button>
        </div>
        {modalOpen && <UploadModal closeModal={closeModal} />}
      </>
    )
}

export default Home