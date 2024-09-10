import { Button} from "flowbite-react";
import { Sidebar } from "flowbite-react";
import { HiChartPie, HiInbox, HiUser, HiViewBoards } from "react-icons/hi";

export default function Head({setThere}) {
    console.log(setThere)
    
  function handleLogout(){
    fetch('/logout',{method:"DELETE"})
    // .then(r=>r.json())
    .then(data => setThere(undefined))
    // .then(()=>navigate('/'))
}
    return(
        <div>
        <Sidebar aria-label="Default sidebar example">
      <Sidebar.Items>
        <Sidebar.ItemGroup>
          <Sidebar.Item href="/buy" icon={HiChartPie}>
            Buy
          </Sidebar.Item>
          <Sidebar.Item href="/monster" icon={HiViewBoards} labelColor="dark">
            Monsters
          </Sidebar.Item>
          <Sidebar.Item href="/media" icon={HiInbox}>
            Movies and episodes
          </Sidebar.Item>
          <Sidebar.Item href="/" icon={HiUser}>
            Home
          </Sidebar.Item>
        </Sidebar.ItemGroup>
      </Sidebar.Items>
    </Sidebar>
            <img src="https://mhcollector.com/wp-content/uploads/2015/02/Original-Ghouls-Collection-6-Pack.jpg" alt="monster high"/>           
            <Button onClick={handleLogout}> Logout </Button>
        </div>
    )

}