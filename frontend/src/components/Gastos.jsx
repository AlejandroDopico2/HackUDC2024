import React from 'react'
import ColumnChart from './ColumnChart'
import LineChart from './LineChart'


function Gastos() {
  return (
    <>
        <div>
            <h1 className='text-green-500 text-3xl'>Gastos</h1>
        </div>

        <div className='flex items-center justify-center h-screen'>
            <div className='container bg-white rounded shadow-md '>
            <ColumnChart/>
            </div>
        </div>

        <div className='flex items-center justify-center h-screen'>
            <div className='container bg-white rounded shadow-md '>
                <LineChart/>
            </div>
        </div>


    </>
  )
}

export default Gastos