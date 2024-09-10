import { useLocation } from 'react-router-dom';

function Details() {
    const location = useLocation();
    const { disMon, indivMon } = location.state || {};

    

    return(
        <>
        <div class="ui card">
  <div class="image">

    <img src="https://i.ebayimg.com/images/g/4jgAAOSwcJxl-Huo/s-l1200.jpg"/>
     </div>
  <div class="content">
    <a class="header">{indivMon.name}</a>
    <div class="meta">
      <span class="date">{indivMon.age}</span>
    </div>
    <div class="description">
     {indivMon.parents}
    </div>
  </div>
</div>

        </>
    )
        }
 

export default Details