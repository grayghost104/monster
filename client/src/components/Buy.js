import { useState, useEffect } from "react"
import { Button} from "flowbite-react";

export default function Buy(){
    const [by, setBy] = useState([])
    useEffect(()=>{
        fetch('/buy')
        .then(r=>{
            if(r.ok){
                return r.json()
            }
            else {
                throw new Error
            }
        })
        .then(data=>{
            setBy(data)
        }) 
    },[])
    const b1 = by[0]
    const b2 = by[1]
    const b3 = by[2]
    const b4 = by[3]
    const b5 = by[4]
  // const byRender = by.map((indivBy)=> {
    //     return(
    //         <div key={indivBy.id}>
    //             <div className='dolls'>{indivBy.dolls}</div>
    //         </div>
    //     )
    // })
    return(
        <>
        {/* {byRender} */}

        <h2><Button className='dolls' href='https://www.ebay.com/itm/386907105801?_skw=monster+high+dolls+g1&hash=item5a1575ea09:g:TOIAAOSw-pZmEfyY&itmprp=enc%3AAQAJAAAA8HoV3kP08IDx%2BKZ9MfhVJKlwawZaIaXevk6w671%2FVLPVnH%2FRkOmrIrc84K%2B0Tz2Fj6XqOtlJhoUXOxR2ZnMHWv%2FTNko6eZPJUVwpDtl1Qr0xGHYV6Ve%2FsO9I1Htk4Pt2pWrtV%2F07x1HDXIhe0nSgWO91A5mAdgSvr0yMYpk7oT26H5xS1B7shi5Dq2IvOHlxeGpHjAS03iSq14NYaS4TZQfdtnty2U%2F1YNcn%2Fibcr8nt5pJHuyrG5qwY732Ai6klQG9XPW5seRqf4cQ1wBeK41N9h%2BsbnBvstYS6%2BpJpxyMvE5PxMOXsMWaIGHCSxswnBA%3D%3D%7Ctkp%3ABFBM6pXIwLxk'>Ghoulia Yelps</Button></h2>
        <h2><Button className='dolls' href='https://www.ebay.com/itm/235724473727?_skw=monster+high+dolls+g1&hash=item36e246057f:g:ujIAAOSwjKBm1Mq5&itmprp=enc%3AAQAJAAAA8HoV3kP08IDx%2BKZ9MfhVJKkOy53%2FK086MLYvEAOFbmHIE1BZJ9Z5Q2TvMXqQlPGu%2B6XOqQ9YggkzVMMADz6H4nl1Tz7KHZstMTD5TFirOEL1EqKjV%2Br8%2BN0gVW5bAoZSktr6kLuKf2Bee%2B5k%2BvRtIcU8FlLznvNCt0AS15tbKiTS2l%2BJcAAhiB2gdjWH%2Bx3ia%2BOTgLay5OA8v7EXKuf2oWU38oRVahXUChHfSSIc9WDI%2BvZFlR8Xb6SAaC0AJ2pz%2B6E9W62pc%2B3%2FWA39Rzc3%2BX4Thwq12hZyvFwBRs27RBqaVFdfyVS8HN4HafnyH%2F4Mrg%3D%3D%7Ctkp%3ABFBM7pXIwLxk'>Assortment of Dolls</Button></h2>
        <h2><Button className='dolls' href='https://www.ebay.com/itm/186177332985?_skw=monster+high+dolls+g1&hash=item2b5908a6f9:g:Y7kAAOSwJxhlXuVh&itmprp=enc%3AAQAJAAAA0HoV3kP08IDx%2BKZ9MfhVJKlAO8JfUXftA59KEDzRocmUftzm0wx1VaZUJRX3xtFSi1bK%2F2%2BikTKVOu4i3OoqS75FsOJZurG29y9UCYSszcZpBgvcNOLKAxbEISwKh92Ky0xl14ReqEgHjEvlYXNKI6%2F31QpZRuPmCCoi6cZrxL5%2FG8B1BNWPs6dqkxvpchJIpSLkz2DwnFDHzJV2%2FOKeow5DYmimMZ97hdZGRUDN%2FmfSM9EwBEaVcsJRKEvPlmOwThXk%2BSJFBJBJTzo%2B4n0o1fo%3D%7Ctkp%3ABk9SR_CVyMC8ZA'>Assortment of Dolls</Button></h2>
        <h2><Button className='dolls' href='https://www.ebay.com/itm/186342032291?_skw=monster+high+dolls+g1&hash=item2b62d9c3a3:g:Ch8AAOSwcE1l8aCH&itmprp=enc%3AAQAJAAAA8HoV3kP08IDx%2BKZ9MfhVJKmQy5avVZOap9pCW17y33LQCCz%2BkvBJ%2Bx1t73kpA9I6Dzm8K3RHZkHuGw0saJziJCM0uzbylV5PSeF6e55qXFM7vWKS9Cu%2BH4d%2B30GJrYKZ8e%2BG28faVGEIc1zYEDXMK4c0NswkPF%2FBIoEURgLJqWlS3SOruI%2B5%2BgfJpUW0buXsc%2Fu%2BRTnDtJiJsFgrRaMj%2BRSv23XJsZngQOKAjTs4pC6%2BMRUohKmwVGyP7YIRMxFAiNsPqAtMK5caCWgu%2FUg%2FTz0zBKJmNI7aE678AViOYLw1LkIf9dkXc%2BaQ6%2BAHaslolg%3D%3D%7Ctkp%3ABk9SR_CVyMC8ZA'>Assortment of Draculauras</Button></h2>
        <h2><Button className='dolls' href='https://www.ebay.com/itm/166949601759?_skw=monster+high+dolls+g1&hash=item26def8c1df:g:~4QAAOSwPxtmjbU7&itmprp=enc%3AAQAJAAAA0HoV3kP08IDx%2BKZ9MfhVJKkGi045Pqe4%2Fb2pDPFQJ8PgvrdYdx3QWrP0DfAFHxd5nm8SKBqNwGjz%2F3htiXWxOWzxQHNvgIBwbdpkwNsN1nmUnUEuzZ4%2BhzXHPHdtbDI81qNL0QEjQ19Tc1SsvQxWKO4U3%2Bi4d7xXA%2BSS3uwiUFXKggTzd8nWZgxt0By0YHJoUYOujTR6wfDaUWOeymqVifgGbOGCLAzh7ZO%2Bee3wVX%2FoM%2BHDl%2BgnRkwmECSbqD9%2ByR1NQlYTnCGLNwy1j%2F9rnNA%3D%7Ctkp%3ABk9SR_CVyMC8ZA'>Draculaura and Clawd</Button></h2>
        
        </>
        
    )
}