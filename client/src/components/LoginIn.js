import { Button, Checkbox, Label, TextInput } from "flowbite-react";
// import React, { useState } from 'react';
// import { Navigate, useNavigate } from 'react-router-dom';

export default function Login({username, setUsername, password, setPassword, user, setUser, sLI, setSLI},e){
  // e.preventDefault();
  // fetch('/login', {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json'
  //   },
  //   body: JSON.stringify({
  //     username: username,
  //     password: password, 
  //     stayLoggedIN: sLI
  //   })
  // })


    
    return(
    <form>
<Label value="Your username" />
        <TextInput onChange={(e) => setUsername(e.target.value)} type='username' id="username"/>
          <Label value="Your password" />
        <TextInput onChange={(e) => setPassword(e.target.value)} type='password' id="password"/>
      <Button variant='primary' type="submit">Login</Button>
      <Button variant='primary' className='mt-3' href='/register'>Create New User</Button>
    </form>
    )
}