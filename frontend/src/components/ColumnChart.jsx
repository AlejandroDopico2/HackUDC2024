import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom'
import anychart from 'anychart';
import axios from 'axios';

const ColumnChart = ({tiempo, fecha}) =>{
  const storedUsername = localStorage.getItem('username');
  const [chart, setChart] = useState(null);

  useEffect(() => {
    console.log("Hola")
    const fetchData = async () => {
      try {
        const seriesData = await getData();

        if (!chart) {
          // Si el gráfico no existe, crea uno nuevo
          const newChart = anychart.column();
          setChart(newChart);
        }

        // Añadir serie de datos al gráfico
        chart.column(seriesData);

        // Configurar opciones y estilos adicionales aquí si es necesario

        // Renderizar el gráfico
        chart.container('container');
        chart.draw();
      } catch (error) {
        console.error("Error al realizar la petición GET de las gráficas: " + error);
      }
    };

    fetchData();

    return () => {
      // Limpiar el gráfico al desmontar el componente
      if (chart) {
        chart.dispose();
        setChart(null);
      }
    };
  }, [chart]);

  async function getData() {
    try {
      const param = {
        username : storedUsername,
        // time : tiempo,
      };
      const response = await axios.get('http://localhost:8000/api/columnChart/', { params:param });
      return response.data;
    } catch (error) {
      console.error("Error al realizar la petición GET de las gráficas: " + error);
      return [];
    }
  }

  return (
    <div className='w-full h-full'>
      {/* Contenedor para el gráfico */}
      <div id="container" className='w-full h-full'></div>
    </div>
  );
}

export default ColumnChart;
