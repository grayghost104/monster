import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
import { Sidebar } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";
// import Create from "./components/Create";
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
  // useEffect(()=>{
  //   fetch('/api/checkse')
  //   .then(r=>{
  //     if (r.ok){
  //       return r.json()
  //     }
  //     else {throw new Error}
  //   })
  //   .then(data=>{
  //     setThere(data)
  //   })
  //   .catch(()=>{})
  // },[])



  // useEffect(() => {
  //   fetch('/api/session')
  //   .then(r=>{
  //     if (r.ok) { return r.json()}
  //     else {throw new Error}
  //   })
  //   .then(data=>{
  //     setUser(data)
  //   })
  //   .catch(data=>{console.log(data)})
      
  // }, [])




//   function handleLogout(){
//     fetch('/api/logout',{method:"DELETE"})
//     .then(r=>r.json())
//     .then(data => setUser(undefined))
//     .then(()=>navigate('/'))
// }



  return(
    <div className="App">
      <BrowserRouter>
      <Head/>
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

// export function Component() {
//   return (
//     <Sidebar aria-label="Default sidebar example">
//       <Sidebar.Items>
//         <Sidebar.ItemGroup>
//           <Sidebar.Item href="#" icon={HiChartPie}>
//             Dashboard
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiViewBoards} label="Pro" labelColor="dark">
//             Kanban
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiInbox} label="3">
//             Inbox
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiUser}>
//             Users
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiShoppingBag}>
//             Products
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiArrowSmRight}>
//             Sign In
//           </Sidebar.Item>
//           <Sidebar.Item href="#" icon={HiTable}>
//             Sign Up
//           </Sidebar.Item>
//         </Sidebar.ItemGroup>
//       </Sidebar.Items>
//     </Sidebar>
  // );


export default App