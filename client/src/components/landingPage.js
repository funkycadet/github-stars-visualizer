import React from 'react'


export const LandingPage = () => {
  return (
    <div>
      <article className='hero-section h-screen mt-20 space-y-14'>
        <h1 className='text-5xl font-bold'>
          A better way to explore your favourite 
          <br></br>programming languages
        </h1>
        <p className='text-2xl text-neutral-500'>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, <br></br>
          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <br></br>
          Dictum non consectetur a erat nam at lectus.
        </p>
        <button className='explore-button'>
          Get Started
        </button>
      </article>
      {/* Get Started section */}
      <article className='get-started flex justify-center flex-col items-center bg-blue-500 w-100%'>
        <h1>
          Get Started in a few minutes
        </h1>
        <p>
          Explore over 90+ repositories from GitHub
        </p>
        <div className='flex flex-row justify-between items-center w-100%'>
          <article>
            Search
          </article>
          <article>Explore</article>
          <article>Start <br></br> Learning</article>
        </div>
      </article>
    </div>
  )
}

export default LandingPage