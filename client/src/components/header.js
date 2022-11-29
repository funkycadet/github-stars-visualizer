import React from 'react'

export const Header = () => {
  return (
      <div className='flex justify-between items-center flex-row  h-10 relative'>
            <h1 className='text-4xl font-bold'>
                GitStars
            </h1>
          <nav>
              <ul className='navlinks flex flex-row justify-evenly'>
                  <li className='hover:underline underline-offset-8'>Home</li>
                  <li className='hover:underline underline-offset-8'>Explore</li>
                  <li className='hover:underline underline-offset-8'>About</li>
                  <li className='hover:underline underline-offset-8'>Contact Us</li>
              </ul>
          </nav>
      </div>
  )
}

export default Header