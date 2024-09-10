import {useEffect, useState} from 'react'
import { Button} from "flowbite-react";
import { useNavigate } from 'react-router-dom' 
import Details from './components/Details';
export default function Monster(){
    const [disMon, setDisMon] = useState([])
    const navigate = useNavigate();
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
    const handleDetails = (indivMon) => {
        navigate('/details', { state: { disMon, indivMon } });
    };

    const monsterRender = disMon.map((indivMon)=> {
        console.log(indivMon)
        return(
            <>
            <div class="ui card">
            </div>
            <div key={indivMon.id}>
                <Button className='name' onClick={() => handleDetails(indivMon)}>{indivMon.name}</Button>
                {/* <div class="content">
                    </div>
                <div className='age'>{indivMon.age}</div>
                <div className='parents'>{indivMon.parents}</div> */}
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