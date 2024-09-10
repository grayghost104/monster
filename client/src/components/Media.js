import { Button } from 'flowbite-react'
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
                throw new Error()
            }
        })
        .then(data=>{
            setMed(data)
        }) 
    },[])


    // console.log(med)
    const mediaRender = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <Button className='movies' href='https://www.imdb.com/list/ls033255959/'>{indivMed.movies}</Button>
            </div>
        )
    })
    const mediaRen = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <Button className='episodes' href='https://www.youtube.com/@MonsterHigh/featured'>{indivMed.episodes}</Button>
            </div>
        )
    })
    return(
        <>
        <h1>Movies</h1>
        {mediaRender}
        <h1>Episodes</h1>
        {mediaRen}
        </>
    )
}


