import {useEffect, useState} from 'react'
import { Button} from "flowbite-react";
import { useNavigate } from 'react-router-dom' 
export default function Story(){
    const [disSto, setSto] = useState([])
    const navigate = useNavigate();

    useEffect(()=>{
        fetch('/story')
        .then(r=>{
            if(r.ok){
                return r.json()
            }
            else {
                throw new Error
            }
        })
        .then(data=>{
            setSto(data)
        }) 
    },[])


    const mediaRender = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <>{indivMed.movies}</>
            </div>
        )
    })




}
