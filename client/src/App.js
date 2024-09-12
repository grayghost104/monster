import React, { useEffect, useState } from "react";
import Media from "./components/Media";
import Buy from "./components/Buy";
import Head from "./Head";
import Account from "./components/Account";
import Details from "./components/Details";
import Monster from "./Monster";
import E_user from "./components/Home";
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
    fetch('/checksessions')
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
          <Route path='/details' element={<Details/>}/>
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