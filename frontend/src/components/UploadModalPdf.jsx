// En tu componente que contiene el modal (por ejemplo, UploadModalPdf.js)
import React, { useState } from 'react';
import axios from 'axios';

const UploadModalPdf = ({ closeModalPdf }) => {
const [file, setFile] = useState(null);
  const storedUsername = localStorage.getItem('username');
  
  const handleFileUpload = async (e) => {
    const selectedFile = e.target.files[0];
    if(selectedFile) {
      try {
        const formData = new FormData();
        formData.append('pdf_file', selectedFile);
  
        
   
        await axios.post(`http://localhost:8000/api/uploadPdf/${storedUsername}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
  
        console.log('Archivo PDF subido exitosamente');
      } catch (error) {
        console.error('Error al subir el archivo PDF:', error);
      }
    }else{
      console.error('No se seleccionó un archivo PDF');
    }
    
    
    closeModalPdf();
  };
  

  return (
    <div className="fixed inset-0 z-50 overflow-auto flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white p-8 rounded-md w-96 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4 text-blue-500">Subir PDF de la factura</h2>
        <input
          type="file"
          onChange={handleFileUpload}
          className="mb-4 p-2 border border-gray-300 rounded-md w-full"
          accept='.pdf'
        />
        <div className="flex justify-end">
          <button
            onClick={closeModalPdf}
            className="bg-blue-500 text-white p-2 rounded-md hover:bg-blue-600 mr-2">
            Cerrar
          </button>
          <button
            onClick={handleFileUpload}
            className="bg-green-500 text-white p-2 rounded-md hover:bg-green-600">
            Subir
          </button>
        </div>
      </div>
    </div>
  );
};

export default UploadModalPdf;
