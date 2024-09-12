import { Button} from "flowbite-react";


function E_user({there, setThere}){




    function handleLogout(){
        fetch('/logout',{method:"DELETE"})
        .then(data => setThere(undefined))
      }
    
    // function handleGone(id){
    //     fetch('/user/${userId}', {
    //         method: 'DELETE',
    //         })
    //         .then(r=>r.json())
    //         .then(data=>{

    //         })
    //     })
    // }



    return(
<>
<Button onClick={handleLogout}> Logout </Button>
</>
    );
}
export default E_user