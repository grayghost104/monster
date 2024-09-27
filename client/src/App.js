import React, { useEffect, useState } from "react";
import Media from "./components/Media";
import Buy from "./components/Buy";
import Head from "./Head";
import Account from "./components/Account";
import Monster from "./Monster";
import E_user from "./components/Home";
import Story from "./components/Story";
import Change from "./components/Change";
import More from "./components/More";
import {
  Routes,
  Route,
  Link,
  BrowserRouter,
  redirect
} from 'react-router-dom'
function App() {
  const [there, setThere] = useState(null);
  useEffect(()=>{
    fetch('http://127.0.0.1:5555/checksessions')
    .then(r=>{
      if (r.ok){
        return r.json()
      }
      else {throw new Error}
    })
    .then(data=>{
      setThere(data)
    })
    .catch(()=>{})
  },[])

  console.log(there)
  return(
    <div className="App">
      <BrowserRouter>
      <Head setThere={setThere} there={there}/>
        <Routes>
          { there ? (
            <>  
          <Route path='/buy' element={<Buy/>}/>
          <Route path='/media' element={<Media/>}/> 
          <Route path="/monster" element={<Monster/> } />
          <Route path='/story' element={<Story/>}/>
          <Route path='/change' element={<Change/>}/>
          <Route path='/more' element={<More/>}/>
          <Route path='/home' element={<E_user there={there} setThere={setThere}/>}/>
             </>
          ): (
            <>
            <Route path='/' element={<Account there={there} setThere={setThere}/>}/> 
             </>
          )}
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App

 // "proxy": "http://localhost:5555"