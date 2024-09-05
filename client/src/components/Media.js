import {useState, useEffect} from 'react'

export default function Media(){
    // https://en.wikipedia.org/wiki/Monster_High_(web_series)
    const [med, setMed] = useState([])
    useEffect(()=>{
        fetch('/media')
        .then(r=>{
            if(r.ok){
                return r.json()
            }
            else {
                throw new Error
            }
        })
        .then(data=>{
            setMed(data)
        }) 
    },[])
    console.log(med)
    const mediaRender = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <div className='movies'>{indivMed.movies}</div>
                <div className='episodes'>{indivMed.episodes}</div>
            </div>
        )
    })
    return(
        <>
        {mediaRender}
        </>
    )
}

