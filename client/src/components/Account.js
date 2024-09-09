import { Button,Label, TextInput } from "flowbite-react";
import { useNavigate } from 'react-router-dom' 
import { useState} from 'react';

function Account({there, setThere}) {
    const navigate = useNavigate()
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [rusername, setRUsername] = useState("");
    const [rpassword, setRPassword] = useState("");
    const [sLI, setSLI] = useState(false);


    function Login(e){
        e.preventDefault();
        fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: username,
            password: password, 
            stayLoggedIN: sLI
          })
        })
        .then(r=>{
          if (r.ok) { return r.json()}
          else {throw new Error()}
        })
        .then(data=>{
          console.log(data)
          setThere(data)
          navigate('/monster')
        })
        .catch(data=>{
          alert('Invalid Username or Password')
        })
    }

    function Create(e){
        e.preventDefault();
        fetch('/api/user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: e.target[1].value,
                password: e.target[2].value,
                fav_mon: e.target[3].value,
                fav_mov: e.target[4].value 
            })
            .then(r => r.json())
            .then(data => {
                if (data.errors == null) {
                    alert("Created Account Successful")
                    navigate('/')
                } else {
                    alert(data.errors)
                }
            })
        })
    }

    // function handleLogout(){
    //     fetch('/api/logout',{method:"DELETE"})
    //     .then(r=>r.json())
    //     .then(data => setUser(undefined))
    //     .then(()=>navigate('/'))
    // }

    return(
        <>
        <h1>Monster High!</h1>
        <h3>Do you have a skullette key(login in)</h3>
        <form onSubmit={Login}>
            <Label value="Your username" />
        <TextInput value={username} onChange={(e) => setUsername(e.target.value)} type='text' id="username"/>
          <Label value="Your skullette key" />
        <TextInput value={password} onChange={(e) => setPassword(e.target.value)} type='text' id="password"/>
        <input type="checkbox" onChange={(e)=>setSLI(!sLI)}/>
      <Button variant='primary' type="submit">Login</Button>
      <Button variant='primary' className='mt-3' type="submit">Create New User</Button>
    </form>
        <h3>Or do you need help of your ghoulfriends to find one?(create an account)</h3>
        <form onSubmit={Create}>
        <Label value="Your username" />
        <TextInput type="text" value={rusername} onChange={(e)=>setRUsername(e.target.value)} placeholder="Username"  id="username"/>
          <Label value="Your skullette key" /> 
        <TextInput id="password"value={rpassword} onChange={(e) => setRPassword(e.target.value)}/>
          <Label value="Favorite Monster High Character" />
        <TextInput id="fav_mon" />
        {/* <Checkbox id="agree" />
        <Label htmlFor="agree" className="flex"/>
          I would like to see the stuff about my favorite&nbsp;
          <Link href="#" className="text-cyan-600 hover:underline dark:text-cyan-500">
            terms and conditions
          </Link> */}
          <Label value="Favorite Monster High Movie" />
        <TextInput id="fav_mov" />
        {/* <Checkbox id="agree" />
        <Label htmlFor="agree" className="flex"/>
        I would like to see the stuff about my favorite movie&nbsp;
          <Link href="#" className="text-cyan-600 hover:underline dark:text-cyan-500">
            terms and conditions
          </Link> */}
           <input type="checkbox" onChange={(e)=>setSLI(!sLI)}/>
      <Button type="submit">Register new account</Button>
    </form>
        
        </>
    )

}
export default Account;