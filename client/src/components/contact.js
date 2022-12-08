import React from 'react'
import Header from './header'
// images svg
import terms from '../images/terms.svg';

export const Contact = () => {
  return (
    <>
    <Header/>
    <div className='contact-container flex justify-center items-center flex-col'>
      <h1 className='text-3xl font-bold tracking-wider'>
        Contact Us
      </h1>
      <p className='mt-4'>
        Any questions, feedback or remarks ? Write us a message !
      </p>
      <div className='form-container flex flex-row w-80% mt-8'>
        <div className='left-form w-1/3'>
          <img src={terms} alt="contact animation"/>
          <h1 className='tracking-wider text-center mt-8'>Fill up the form and our team would get back to you!</h1>
        </div>
        <div className='right-form w-2/3'>

        </div>
      </div>
    </div>
    </>
  )
}

export default Contact