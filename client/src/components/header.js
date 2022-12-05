import React from 'react'
// image import
import starsLogo from '../images/logo.svg'
import { useState } from 'react';
// import from react-router
import { Link } from 'react-router-dom';

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
                    <img className='mt-2 ml-1' src={starsLogo} alt="logo" height="2rem"/>
                </span>
            </h1>
          <nav>
              <ul className='navlinks flex flex-row justify-evenly text-xl'>
                  <li><Link to="/">Home</Link></li>
                  <li><Link to="/explore">Explore</Link></li>
                  <li><Link to="/about">About</Link></li>
                  <li><Link to="/contact">Contact us</Link></li>
              </ul>
          </nav>
      </div>
  )
}

export default Header