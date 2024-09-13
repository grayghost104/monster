import {useEffect, useState} from 'react'
import {Label} from "flowbite-react";

export default function Monster(){
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
  
    const monsterRender = disMon.map((indivMon)=> {
        // console.log(disMon)
        return(
            <>
            <div class="ui card">
            </div>
            <div key={indivMon.id}>
                <img src ={indivMon.img}/>
                <h1>{indivMon.name}</h1>

                <div class="content">
                    </div>
                    <h3>Age</h3>
                <div className='age' >{indivMon.age}</div>
                <h3>Parents</h3>
                <div className='parents'>{indivMon.parents}</div>
                <h3>Friends</h3>
                <div className='friends'>{indivMon.friends}</div>
                <h3>Enemies</h3>
                <div className='enemies'>{indivMon.enemies}</div>
                <h3>Movies they are in</h3>
                <div className='movies'>{indivMon.movies}</div>
            </div>
            </>
        )
    })
    return(
        <div>
            {monsterRender}
        </div>
    )
}