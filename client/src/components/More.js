import React from "react";
import { Button,Label, TextInput } from "flowbite-react";
import {useEffect, useState} from 'react'


function More(){
    const [more, setMore] = useState([])
    const [movies, setMovies] = useState("")
    const [episodes, setEpisodes] = useState("")
    
    const [editingmedia, setEditingMedia] = useState(null)
    const [newEpisodes, setNewEpisodes] = useState("")
    const [newMovies, setNewMovies] = useState("")

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
            setMore(data)
        }) 
    },[])

    
    function addMedia(){
        fetch("/media",{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body: JSON.stringify({movies: movies, episodes: episodes})
        })
        .then(r=>r.json())
        .then(data=>{
          const newMedia = [...more, data]
          setMore(newMedia)
        })
    }

    const deleteMedia = (mediaId) => {
        fetch(`/media/${mediaId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to delete media');
            }
            return response.json(); // Handle response if needed
        })
        .then(() => {
            const updatedMedia = more.filter(media => media.id !== mediaId);
            setMore(updatedMedia);
        })
        .catch(error => {
            console.error('Error deleting media:', error);
        });
    };


    const handleEdit = (mediaId) => {
        fetch(`/media/${mediaId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                movies: newMovies,
                episodes: newEpisodes
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update media');
            }
            return response.json();
        })
        .then(updatedMedia => {
            const updatedMedias = more.map(media =>
                media.id === mediaId ? updatedMedia : media
            );
            setMore(updatedMedias);
            setEditingMedia(null); // Close the form
        })
        .catch(error => {
            console.error('Error updating media:', error);
        });
    };
    const startEditing = (media) => {
        setEditingMedia(media.id);
        setNewMovies(media.movies);
        setNewEpisodes(media.episodes);
    };
   
    return(
        <>
         <div>
            <ul>
                <h2>Movies</h2>
                {more.map(media => (
                    <li key={media.id}>
                        
                        {media.movies}
                        {media.episodes}
                        <button onClick={() => startEditing(media)}>Edit</button>
                    </li>
                ))}
            </ul>
            {editingmedia && (
                <div>
                    <h3>Edit media</h3>
                    <form
                        onSubmit={(e) => {
                            e.preventDefault();
                            handleEdit(editingmedia);
                        }}
                    >
                        <div>
                            <label>
                                Movies:
                                <input type="text" value={newMovies} onChange={(e) => setNewMovies(e.target.value)}/>
                            </label>
                        </div>
                        <div>
                            <label>
                                Episodes:
                                <input type="text" value={newEpisodes} onChange={(e) => setNewEpisodes(e.target.value)}/>
                            </label>
                        </div>
                        <button type="submit">Update</button>
                        <button type="button" onClick={() => setEditingMedia(null)}>Cancel</button>
                    </form>
                </div>
            )}
        </div>
        <div>
            <ul>
                {more.map(media => (
                    <li key={media.id}>
                        <Label value={media.movies} />
                        <Label value={media.episodes} />
                        <button onClick={() => deleteMedia(media.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
         <form onSubmit={addMedia}>
            <Label value="Movies" />
        <TextInput value={movies} onChange={(e) => setMovies(e.target.value)} type='text' id="movies"/>
          <Label value="Episodes" />
        <TextInput value={episodes} onChange={(e) => setEpisodes(e.target.value)} type='text' id="episodes"/>
      <Button variant='primary' classmovies='mt-3' type="submit">Add your the pieces of brain to the jar of this webiste</Button>
    </form>
        </>
    );
}

export default More