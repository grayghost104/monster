import {useEffect, useState} from 'react'

export default function Monster(){
    // indivMon, disMon, setDisMon

    const [disMon, setDisMon] = useState([])

    // https://shop.mattel.com/search?q=monster+high#filter.ss_filter_tags_super_category=Dolls%20&%20Dollhouses/filter.ss_brand=Monster%20High/filter.ss_filter_tags_web_category=Dolls
    // https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0
    useEffect(()=>{
        fetch('/monster')
        .then(r=>{
            if(r.ok){
                return r.json()
            }
            else {
                throw new Error
            }
        })
        .then(data=>{
            setDisMon(data)
        }) 
    },[])

    console.log(disMon)

    const monsterRender = disMon.map((indivMon)=> {
        return(
            <div key={indivMon.id}>
                <div className='name'>{indivMon.name}</div>
                <div className='age'>{indivMon.age}</div>
                <div className='parents'>{indivMon.parents}</div>
                <span>
                    <i className='movies'/>
                    {indivMon.movies}
                </span>
            </div>
        )
    })

    return(
        <div>
            <img src='https://m.media-amazon.com/images/I/81uTGf+SNGL._AC_UF894,1000_QL80_.jpg'/>
            <img src='https://m.media-amazon.com/images/I/61NKUBVAoKL._AC_UF894,1000_QL80_.jpg'/>
            {monsterRender}

        </div>
    )
}