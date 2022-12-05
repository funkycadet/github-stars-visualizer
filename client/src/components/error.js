import React from 'react'
// image import
import errorimg from '../images/error-404.svg'
// import from react router dom
import { Link } from 'react-router-dom'


 
export const Error = () => {
  
  return (
    <div className='flex justify-center flex-col items-center w-100% h-screen'>
        <img id="error-image" src={errorimg} alt="errorimage"/>
        <h1>404 Error</h1>
        <h2>Page not found</h2>
        <Link to="/" className='text-red-500'>Go back to home page -&gt;</Link>
    </div>
  )
}

export default Error