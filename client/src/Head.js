import { Sidebar } from "flowbite-react";
import { BiBuoy } from "react-icons/bi";
import { useEffect } from "react";
import { HiChartPie, HiInbox, HiUser, HiViewBoards, HiArrowSmRight } from "react-icons/hi";

export default function Head({setThere}) {
    console.log(setThere)
    const background = document.body.style.backgroundImage = "url('https://i.pinimg.com/736x/1d/dc/44/1ddc445b323bdde94ae2b3be6941bf9b.jpg')";
    useEffect(() => {
      document.body.style.backgroundImage = "url('https://i.pinimg.com/736x/1d/dc/44/1ddc445b323bdde94ae2b3be6941bf9b.jpg')";
      
      // Cleanup background image on component unmount
      return () => {
          document.body.style.backgroundImage = "";
      };
  }, []);

  // Video iframe as a constant
  const videoIframe = (
      <iframe
          width="1280"
          height="720"
          src="https://www.youtube.com/embed/yM54tXtXAoQ"
          title="Opening | Monster High Ghouls Rule"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          referrerPolicy="strict-origin-when-cross-origin"
          allowFullScreen
      ></iframe>
  );
    // const obj = {"video":{
    //   "value" : '<iframe width="1280" height="720" src="https://www.youtube.com/embed/yM54tXtXAoQ" title="Opening | Monster High Ghouls Rule" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    // }}
    // const vid = document.write(obj.video.value)
    return(
      <>
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
          <Sidebar.Item href="/story" icon={HiArrowSmRight}>
            Story
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
    {/* <img src='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f34be48a-0d41-4f5e-b7ca-f973db286eb8/d58yqwh-98bd4ebf-79b8-4dc8-aec6-27a53fccb242.jpg/v1/fill/w_800,h_413,q_75,strp/monster_high_background_pattern_by_thestralwizard_d58yqwh-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDEzIiwicGF0aCI6IlwvZlwvZjM0YmU0OGEtMGQ0MS00ZjVlLWI3Y2EtZjk3M2RiMjg2ZWI4XC9kNTh5cXdoLTk4YmQ0ZWJmLTc5YjgtNGRjOC1hZWM2LTI3YTUzZmNjYjI0Mi5qcGciLCJ3aWR0aCI6Ijw9ODAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.W1nbAD1HMqYNv67N5spKDBROE4kxo9pELob9Sp2RhVI'/> */}
            {/* <img src="https://mhcollector.com/wp-content/uploads/2015/02/Original-Ghouls-Collection-6-Pack.jpg" alt="monster high"/>            */}
        </div>
        <>
        {videoIframe}
    {/* {vid} */}
        </>
        </>
    )

}

// postgresql://your_monster_high_user:p4Gg8Zd5PDPGyE1vALYljJo5G5cRjLOJ@dpg-crpidrdsvqrc738rmpdg-a.oregon-postgres.render.com/your_monster_high