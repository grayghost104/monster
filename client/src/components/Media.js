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

    // function handleAdd(e){
    //     e.preventDefault();
    //     fetch('/medis', {
    //         method: 'POST',
    //         headers: {
    //           'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify({
    //             movies: movies, 
    //             episodes: episodes
    //         })
    //         .then(r=>r.json())
    //         .then(data=>{
    //             const newArr = [...med, data]
    //             setMed(newArr)
    //         })  
    //     })
    // }


    // function handleEdit() {
    //     fetch(`api/`, {
    //       method: "PATCH",
    //       headers: {
    //         "Content-Type": "Application/json"
    //       },
    //       body: JSON.stringify({
    //         pants: Pants,
    //         shirts: Shirts,
    //         other_clothes: Other_Clothes
    //       })
    //     })
    //       .then(r => r.json())
    //       .then(updatedLug => {
    //         const newArr = projects.map(project => {
    //           if (project.id === updatedProject.id) {
    //             return updatedProject
    //           }
    //           return project
    //         })
    //         setProjects(newArr)
    //       })
    //   }


    // console.log(med)
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
        <h1>G1 Movies and Episodes</h1>
        <h2><Button className='movies' href='https://www.imdb.com/list/ls033255959/'>Movies</Button></h2>
        {mediaRender}
        <h2><Button className='episodes' href='https://www.youtube.com/@MonsterHigh/featured'>Episodes</Button></h2>
        {mediaRen}

        <>
        {/* <form onSubmit={handleAdd}>
            <Label value="Your username" />
        <TextInput value={fdjslf} onChange={(e) => setUsername(e.target.value)} type='text' id="username"/>
          <Label value="Your skullette key" />
        <TextInput value={password} onChange={(e) => setPassword(e.target.value)} type='text' id="password"/>
        <input type="checkbox" name='stayLoggedIn' value={sLI} onChange={e=>setSLI(!sLI)}/>
      <Button variant='primary' type="submit">Login</Button>
      <Button variant='primary' className='mt-3' type="submit">Create New User</Button>
    </form> */}
        </>
        </>
    )
}


