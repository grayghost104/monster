import { Button} from "flowbite-react";
import { Sidebar } from "flowbite-react";
import { BiBuoy } from "react-icons/bi";
import { HiChartPie, HiInbox, HiUser, HiViewBoards } from "react-icons/hi";

export default function Head({setThere}) {
    console.log(setThere)
  
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
            Login/Register
          </Sidebar.Item>
          <Sidebar.Item href="/home" icon={BiBuoy}>
            Home
          </Sidebar.Item>
        </Sidebar.ItemGroup>
      </Sidebar.Items>
    </Sidebar>
            <img src="https://mhcollector.com/wp-content/uploads/2015/02/Original-Ghouls-Collection-6-Pack.jpg" alt="monster high"/>           
        </div>
    )

}