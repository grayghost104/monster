import { useLocation } from 'react-router-dom';

function Details() {
    const location = useLocation();
    const { disMon, indivMon } = location.state || {};

    console.log(disMon)
    return(
        <>
        <div class="ui card">
  <div class="image">
     <img class= 'Jinafire' src="https://i.ebayimg.com/images/g/4jgAAOSwcJxl-Huo/s-l1200.jpg"/>
    {/* <img  class='Abbey'src="https://m.media-amazon.com/images/I/614awBAhPVL.jpg"/>
    <img class = 'Clawdeen' src="https://i.ebayimg.com/images/g/Z6UAAOSw0e9U1o34/s-l1200.jpg"/>
    <img class='Robecca Steam' src="https://m.media-amazon.com/images/I/81PA-XqAMzL._AC_UF894,1000_QL80_.jpg"/>
    <img class='Cleo de Nile' src="https://m.media-amazon.com/images/I/71N74VNOibL._AC_UF894,1000_QL80_.jpg"/>
    <img class='Deuce Gorgon' src="https://m.media-amazon.com/images/I/61EYMnDPb2L.jpg"/>
    <img class='Draculaura' src="https://i.ebayimg.com/images/g/RiUAAOSwiR5lW5ZG/s-l1600.jpg"/>
    <img class='Frankie Stein'src="https://creations.mattel.com/cdn/shop/files/fps9qdk0xof4hz8joei2_ee5b6115-16fd-4a78-9d95-7dbf27e98d32.jpg?v=1718925454"/>
    <img class="Ghoulia Yelps"src="https://m.media-amazon.com/images/I/714BR88IRzL._AC_UF894,1000_QL80_.jpg"/>
    <img class="Lagoona Blue" src="https://i5.walmartimages.com/seo/Monster-High-Lagoona-Blue-Doll-Collectible-Reproduction-in-Original-Look-with-Diary-Doll-Stand_ca33767a-ae05-4a98-9d91-40e104d88de9.12b4bb645febd33d46f30b97243a9e7c.jpeg"/>
    <img class="Heath Burns" src="https://3.bp.blogspot.com/-CDvaP2hJnr0/VuqMpfiZMeI/AAAAAAAAh6c/gRUyuR-dYEkALNllaI9RXvWmztM9zgAWw/s800/Classroom-Abbey-Heath-2-pack-1-Heath.jpg"/>
    <img class="Invisi Billy" src="https://down-br.img.susercontent.com/file/br-11134201-23010-ma8i06rpvfmv96"/>  */}
     </div>
  <div class="content">
    <a class="header">{indivMon}</a>
    <div class="meta">
      <span class="date">{indivMon}</span>
    </div>
    <div class="description">
     {indivMon}
    </div>
  </div>
</div>

        </>
    )
        }
 

export default Details