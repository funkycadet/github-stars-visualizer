// component imports
import {LandingPage} from './components/landingPage'
import {Explore} from './components/explore'
import {About} from './components/about'
import {Contact} from './components/contact'
import {Error} from './components/error'
import {Routes, Route} from "react-router-dom"
// import { useState } from 'react';

function App() {
  return (
    <div className="App w-100%">
      <Routes>
        <Route path='/' element={<LandingPage/>}/>
        <Route path='/explore' element={<Explore/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/contact' element={<Contact/>}/>
        <Route path="*" element={<Error/>}/>
      </Routes>
    </div>
  );
}

export default App;
