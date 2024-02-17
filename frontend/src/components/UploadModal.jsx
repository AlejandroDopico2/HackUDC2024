// En tu componente que contiene el modal (por ejemplo, UploadModal.js)
import React, { useState } from 'react';

const UploadModal = ({ closeModal }) => {
  const handleFileUpload = (e) => {
    // Aquí puedes manejar la lógica para subir el archivo
    // Puedes acceder al archivo con e.target.files[0]
    console.log('Archivo subido:', e.target.files[0]);

    // Cierra el modal después de subir el archivo
    closeModal();
  };

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className="bg-white p-8 rounded-md w-96">
        <h2 className="text-2xl font-semibold mb-4">Subir Archivo</h2>
        <input
          type="file"
          onChange={handleFileUpload}
          className="mb-4"
        />
        <button
          onClick={closeModal}
          className="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600">
          Cerrar
        </button>
      </div>
    </div>
  );
};

export default UploadModal;
