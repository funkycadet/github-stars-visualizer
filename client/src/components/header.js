import React from 'react'

export const Header = () => {
  return (
      <div className='flex justify-between items-center flex-row w-100% h-10 relative'>
            <h1 className='text-4xl font-bold'>
                GitStars
            </h1>
          <nav>
              <ul className='navlinks flex flex-row justify-evenly'>
                  <li>Home</li>
                  <li>Explore</li>
                  <li>About</li>
                  <li>Contact Us</li>
              </ul>
          </nav>
      </div>
  )
}

export default Header