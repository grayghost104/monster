import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";
import { Sidebar } from "flowbite-react";
import { HiArrowSmRight, HiChartPie, HiInbox, HiShoppingBag, HiTable, HiUser, HiViewBoards } from "react-icons/hi";
import Create from "./components/Create";
import Media from "./components/Media";
import Monster from "./components/Monster";
import Buy from "./components/Buy";
import Head from "./Head";
import Login from "./components/LoginIn";
import {
  Routes,
  RouterProvider,
  Route,
  Link,
  BrowserRouter,
  createBrowserRouter,
  redirect
} from 'react-router-dom'

function App() {
  const [password, setPassword] = useState("")
  const [username, setUsername] = useState("")
  const [user, setUser] = useState(null)
  const [sLI, setSLI] = useState(false)
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

  const router = createBrowserRouter([
    {
      path: "/",
      element: <Login 
      username={username} setUsername={setUsername} 
                password={password} setPassword={setPassword} 
                user={user} setUser={setUser} sLI ={sLI} setSLI ={setSLI}
                />
    },
    {
      path: "/create",
      element: <Create/>,
    },
    {
      path: "/monster",
      element: <Monster/>,
      loader: () => {
        return user ? true: redirect("/")
       }
    }
    // {
    //   path: "/media",
    //   element: <Media/>,
    //   loader: () => {
    //     return user ? true: redirect("/")
    //    }
    // },
    // {
    //   path: "/buy",
    //   element: <Buy/>,
    //   loader: () => {
    //     return user ? true: redirect("/")
    //    }
    // },
    // {
    //   path: "/user",
    //   element: <User/>,
    //   loader: () => {
    //     return user ? true: redirect("/")
    //    }
    // }
  ])
  return (
    <div>

    <RouterProvider router={router}/>
    </div>
  )



//   return(
//     <div className="App">
//       <BrowserRouter>
//       <Head/>
//         <Routes>
//           <Route path='/buy' element={<Buy/>}/>
//           <Route path='/media' element={<Media/>}/> 
//           <Route path="/monster" element={<Monster/> } />
//         </Routes>
//       </BrowserRouter>
//     </div>
//   )
// }

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
}

export default App