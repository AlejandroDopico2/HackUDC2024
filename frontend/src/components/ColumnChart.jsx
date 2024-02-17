import React, { useEffect } from 'react'
import anychart from 'anychart';
import anychartReact from 'anychart-react';
import axios from 'axios';

function ColumnChart() {
    
    useEffect(() => {
        // Crear el gráfico AnyChart
        const chart = anychart.column();
    
        // Llamar a la función asincrónica dentro de useEffect
        const fetchData = async () => {
            try {
                // Configurar datos esperando la respuesta de la petición GET
                const seriesData = await getData();
    
                // Añadir serie de datos al gráfico
                const series = chart.column(seriesData);
    
                // Configurar opciones y estilos adicionales aquí si es necesario
    
                // Renderizar el gráfico
                chart.container('container');
                chart.draw();
            } catch (error) {
                console.error("Error al realizar la petición GET de las gráficas: " + error);
            }
        };
    
        // Llamar a la función de fetchData
        fetchData();
    
        // Limpieza al desmontar el componente
        return () => chart.dispose();
    }, []);

      async function getData(){

        try {
            const response = await axios.get('http://localhost:8000/api/columnChart/');
            
            return response.data;
        } catch (error) {
            console.error("Error al realizar la petición GET de las gráficas: " + error);
            return [];
        }
      }
    
      return (
        <div>
          {/* Contenedor para el gráfico */}
          <div id="container" style={{ width: '100%', height: '400px' }}></div>
        </div>
      );
}

export default ColumnChart