import React from 'react'
// images for hero section
import search from '../images/search.svg';
import explore from '../images/explore.svg';
import learn from '../images/learn.svg';
import line from '../images/horizontal-line.svg';
// images for graph section
import bar from '../images/bar-chart.svg';
import linechart from '../images/line-chart.svg';
import pie from '../images/pie-chart.svg';



export const LandingPage = () => {
  return (
    <div className=' space-y-20'>
      <article className='hero-section h-screen mb-10 space-y-14'>
        <h1 className='hero-leading text-6xl font-bold'>
          Explore like never before <br></br>
          Made for Developers, <span id='hero-span'>by Developers.</span>
        </h1>
        <button className='explore-button'>
          Get Started
        </button>
      </article>
      {/* About us section */}
      <div className='about-section'>
        <h1 className='text-center text-3xl'>
          Visualise your preferred language by repositories
        </h1>
        <article className='flex justify-evenly flex-row items-center w-90% space-x-4 p-10'>
          <div className='graph-container flex justify-center items-center'>
            <img src={bar} alt="bar-chart" height={150} width={150} />
          </div>
          <div className='graph-container flex justify-center items-center'>
            <img src={linechart} alt="line-chart" height={150} width={150} />
          </div>
          <div className='graph-container flex justify-center items-center'>
            <img src={pie} alt="pie-chart" height={150} width={150} />
          </div>
        </article>
      </div>
      {/* Small Feature description section */}
      <article className='feature-section flex justify-center flex-col items-center w-100% space-y-4 p-8 relative'>
        <p className='feature-paragraph text-3xl text-white text-center'>
          GitStars is made for developers and tech enthusiasts eager <br></br>
          to expand their knowledge on their <br></br>
          favourite programming languages by familiarising with popular repositories.
        </p>
      </article>
      <div class="blankDiv">
      </div>
      {/* Get Started section */}
      <article className='get-started flex justify-center flex-col items-center w-100% space-y-6 p-8'>
        <h1 className='text-5xl font-bold'>
          Get started in a few minutes
        </h1>
        <p className='text-xl'>
          Explore over 90+ repositories from GitHub
        </p>
        <div className='flex flex-row justify-evenly items-center w-100% space-x-16'>
          <div className='space-y-6 flex flex-col justify-center items-center text-center'>
            <img src={search} alt="search" height={90} width={90} fill="red" />
            <h1 className=' text-2xl'>Search</h1>
          </div>
          <img src={line} alt="line" />
          <div className='space-y-6 flex flex-col justify-center items-center text-center'>
            <img src={explore} alt="explore" height={90} width={90} />
            <h1 className=' text-2xl'>Explore</h1>
          </div>
          <img src={line} alt="line" />
          <div className='space-y-6 flex flex-col justify-center items-center text-center'>
            <img src={learn} alt="learn" height={90} width={90} />
            <h1 className='text-2xl'>Learn more</h1>
          </div>
        </div>
      </article>
      <div className='text-center'>
        <button className='explore-button'>
          Get Started
        </button>
      </div>

    </div>
  )
}

export default LandingPage