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



    
    const storyRender = disSto.map((indivSto)=> {
        return(
            <div key={indivSto.id}>
                <h1>{indivSto.mon_name}</h1>
                <h3>Origin Story</h3>
                <p1>{indivSto.origin_story}</p1>
                <h3>G1</h3>
                <p2>{indivSto.L_book}</p2>
            </div>
        )
    })



    return(
        <div>
            <Button onClick={() => navigate('/change')}>Want to add some of your brains into a story?</Button>
            <Button onClick={() => navigate('/change')}>Want erases this story off this earth???</Button>
            <Button onClick={() => navigate('/change')}>Want to add some of your own horros?</Button>
            {storyRender}
        </div>
    )




}
