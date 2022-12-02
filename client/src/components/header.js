import React from 'react'
import starsLogo from '../images/logo.svg'
import { useState } from 'react';

export const Header = () => {
    const [shadow, setShadow] = useState(false);
    function addShadow(){
      if (window.scrollY >= 22){
        setShadow(true);
      }else {
        setShadow(false);
      }
    }
    window.addEventListener("scroll", addShadow);

  return (
      <div className={shadow ? 'header shadow' : 'header'}>
            <h1 className='text-4xl font-bold inline flex flex-row items-center'>
                GitStars
                <span>
                    <img className='mt-2 ml-1' src={starsLogo} alt="logo"/>
                </span>
            </h1>
          <nav>
              <ul className='navlinks flex flex-row justify-evenly text-xl'>
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