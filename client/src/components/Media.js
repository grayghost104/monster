import { Button } from 'flowbite-react'
import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom' 
export default function Media(){
    // https://en.wikipedia.org/wiki/Monster_High_(web_series)
    const [med, setMed] = useState([])
    const navigate = useNavigate();
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

    const mediaRender = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <>{indivMed.movies}</>
            </div>
        )
    })
    const mediaRen = med.map((indivMed)=> {
        return(
            <div key={indivMed.id}>
                <>{indivMed.episodes}</>
            </div>
        )
    })
    return(
        <>
        <Button onClick={() => navigate('/more')}>Want to add some of your brains into a movie/episode?</Button>
        <Button onClick={() => navigate('/more')}>Want erases this movie/episode off this earth???</Button>
        <Button onClick={() => navigate('/more')}>Want to add some of your own screams?</Button>
        <h1>G1 Movies and Episodes</h1>
        <h2><Button className='movies' href='https://www.imdb.com/list/ls033255959/'>Movies</Button></h2>
        {mediaRender}
        <h2><Button className='episodes' href='https://www.youtube.com/@MonsterHigh/featured'>Episodes</Button></h2>
        {mediaRen}
        </>
    )
}


