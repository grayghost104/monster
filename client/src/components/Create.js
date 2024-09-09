import { Button, 
  // Checkbox,
   Label, TextInput } from "flowbite-react";
// import { Navigate, useNavigate } from 'react-router-dom';

function Create({username, setUsername, password, setPassword, user, setUser, sLI, setSLI}) {

  return (
    <form onSubmit={(e) => {
        e.preventDefault()
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
        })
            .then(r => r.json())
            .then(data => {
                if (data.errors == null) {
                    alert("Created Account Successful")
                    // nav('/')
                } else {
                    alert(data.errors)
                }
            })

    }}>
          <Label value="Your username" />
        <TextInput type="text" value={username} onChange={(e)=>setUsername(e.target.value)} placeholder="Username"  id="username"/>
          <Label value="Your password" />
        <TextInput id="password"/>
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
      <Button type="submit">Register new account</Button>
    </form>
  );
}
export default Create