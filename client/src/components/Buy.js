import { useState, useEffect } from "react"

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
    console.log(by)
    const byRender = by.map((indivBy)=> {
        return(
            <div key={indivBy.id}>
                <div className='dolls'>{indivBy.dolls}</div>
            </div>
        )
    })
    return(
        <>
        {byRender}
        </>
    )
}