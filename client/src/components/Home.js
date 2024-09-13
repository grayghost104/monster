import { Button} from "flowbite-react";


function E_user({there, setThere}){




    function handleLogout(){
        fetch('/logout',{method:"DELETE"})
        .then(data => setThere(undefined))
      }


    return(
<>
<h1>Welcome {there.username}!!</h1>
<h2>Favorite Media: {there.fav_mov}</h2>
<h2>Favorite Monster: {there.fav_mon}</h2>
<Button onClick={handleLogout}> Logout </Button>
</>
    );
}
export default E_user