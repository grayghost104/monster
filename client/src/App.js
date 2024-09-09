import React, { useEffect, useState } from "react";
import Media from "./components/Media";
import Monster from "./components/Monster";
import Buy from "./components/Buy";
import Head from "./Head";
import Account from "./components/Account";
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
      <Head setThere={setThere}/>
        <Routes>
          { there ? (
            <> 
          <Route path='/buy' element={<Buy/>}/>
          <Route path='/media' element={<Media/>}/> 
          <Route path="/monster" element={<Monster/> } />
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