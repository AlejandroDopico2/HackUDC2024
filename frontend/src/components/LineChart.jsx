import React, { useEffect, useState } from 'react';
import anychart from 'anychart';
import 'anychart/dist/css/anychart-ui.min.css';
import 'anychart/dist/fonts/css/anychart-font.min.css';

function LineChart() {
  const [chart, setChart] = useState(null);

  useEffect(() => {
    anychart.onDocumentReady(function () {
      // Solo crea el gráfico si aún no existe
      if (!chart) {
        var dataSet = anychart.data.set(getData());

        var firstSeriesData = dataSet.mapAs({ x: 0, value: 1 });
        var secondSeriesData = dataSet.mapAs({ x: 0, value: 2 });
        var thirdSeriesData = dataSet.mapAs({ x: 0, value: 3 });

        var newChart = anychart.line();
        newChart.animation(true);
        newChart.padding([10, 20, 5, 20]);
        newChart.crosshair().enabled(true).yLabel(false).yStroke(null);
        newChart.tooltip().positionMode('point');
        newChart.title('Trend of Sales of the Most Popular Products of ACME Corp.');
        newChart.yAxis().title('Number of Bottles Sold (thousands)');
        newChart.xAxis().labels().padding(5);

        var firstSeries = newChart.line(firstSeriesData);
        firstSeries.name('Brandy');
        firstSeries.hovered().markers().enabled(true).type('circle').size(4);
        firstSeries
          .tooltip()
          .position('right')
          .anchor('left-center')
          .offsetX(5)
          .offsetY(5);

        var secondSeries = newChart.line(secondSeriesData);
        secondSeries.name('Whiskey');
        secondSeries.hovered().markers().enabled(true).type('circle').size(4);
        secondSeries
          .tooltip()
          .position('right')
          .anchor('left-center')
          .offsetX(5)
          .offsetY(5);

        var thirdSeries = newChart.line(thirdSeriesData);
        thirdSeries.name('Tequila');
        thirdSeries.hovered().markers().enabled(true).type('circle').size(4);
        thirdSeries
          .tooltip()
          .position('right')
          .anchor('left-center')
          .offsetX(5)
          .offsetY(5);

        newChart.legend().enabled(true).fontSize(13).padding([0, 0, 10, 0]);

        setChart(newChart);
      }
    });
  }, [chart]); // Dependencia para evitar recrear el gráfico en cada renderizado

    
      function getData() {
        return [
            ['1986', 3.6, 2.3, 2.8, 11.5],
            ['1987', 7.1, 4.0, 4.1, 14.1],
            ['1988', 8.5, 6.2, 5.1, 17.5],
            ['1989', 9.2, 11.8, 6.5, 18.9],
            ['1990', 10.1, 13.0, 12.5, 20.8],
            ['1991', 11.6, 13.9, 18.0, 22.9],
            ['1992', 16.4, 18.0, 21.0, 25.2],
            ['1993', 18.0, 23.3, 20.3, 27.0],
            ['1994', 13.2, 24.7, 19.2, 26.5],
            ['1995', 12.0, 18.0, 14.4, 25.3],
            ['1996', 3.2, 15.1, 9.2, 23.4],
            ['1997', 4.1, 11.3, 5.9, 19.5],
            ['1998', 6.3, 14.2, 5.2, 17.8],
            ['1999', 9.4, 13.7, 4.7, 16.2],
            ['2000', 11.5, 9.9, 4.2, 15.4],
            ['2001', 13.5, 12.1, 1.2, 14.0],
            ['2002', 14.8, 13.5, 5.4, 12.5],
            ['2003', 16.6, 15.1, 6.3, 10.8],
            ['2004', 18.1, 17.9, 8.9, 8.9],
            ['2005', 17.0, 18.9, 10.1, 8.0],
            ['2006', 16.6, 20.3, 11.5, 6.2],
            ['2007', 14.1, 20.7, 12.2, 5.1],
            ['2008', 15.7, 21.6, 10, 3.7],
            ['2009', 12.0, 22.5, 8.9, 1.5]
          ];
      }
    
      return (
        <div id="second-chart-container" style={{ width: '100%', height: '100%' }}></div>
      );
}

export default LineChart