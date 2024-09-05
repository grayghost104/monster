import {Link} from 'react-router-dom'

export default function Head(){
    return(
        <div>
            <img src="https://snworksceo.imgix.net/bsd/ab50bb2e-e153-466f-a916-16c4a799a82c.sized-1000x1000.webp?w=1000" alt="monster high"/>           
            <Link to='/buy'>Buy</Link>
            <Link to="/media">Movies and episodes</Link>
            <Link to="/monster">All Monsters</Link>
        </div>
    )

}