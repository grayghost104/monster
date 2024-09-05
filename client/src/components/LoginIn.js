import { Button, 
    // Checkbox, 
    Label, TextInput } from "flowbite-react";
// import { Navigate, useNavigate } from 'react-router-dom';

export default function Login({username, setUsername, password, setPassword, user, setUser, sLI, setSLI}){
    // const nav = useNavigate()


    
    return(
    <form>
<Label value="Your username" />
        <TextInput onChange={(e) => setUsername(e.target.value)} type='username' id="username"/>
          <Label value="Your password" />
        <TextInput nChange={(e) => setPassword(e.target.value)} type='password' id="password"/>
      <Button variant='primary' type="submit">Login</Button>
      <Button variant='primary' className='mt-3' href='/register'>Create New User</Button>
    </form>
    )
}