import React from "react";
import { Button,Label, TextInput } from "flowbite-react";
import {useEffect, useState} from 'react'


function Change(){
    const [change, setChange] = useState([])
    const [name, setName] = useState("")
    const [og_story, setOg_story] = useState("")
    const [book, setBook] = useState("")
    
    const [editingStory, setEditingStory] = useState(null)
    const [newName, setNewName] = useState("")
    const [newOg_story, setNewOg_story] = useState("")
    const [newBook, setNewBook] = useState("")

    useEffect(()=>{
        fetch('/story')
        .then(r=>{
            if(r.ok){
                return r.json()
            }
            else {
                throw new Error()
            }
        })
        .then(data=>{
            setChange(data)
        }) 
    },[])

    
    function addStory(){
        fetch("/story",{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body: JSON.stringify({mon_name: name, origin_story: og_story, L_book: book})
        })
        .then(r=>r.json())
        .then(data=>{
          const newStory = [...change, data]
          setChange(newStory)
        })
    }

    const deleteStory = (storyId) => {
        fetch(`/story/${storyId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to delete story');
            }
            return response.json(); // Handle response if needed
        })
        .then(() => {
            const updatedStories = change.filter(story => story.id !== storyId);
            setChange(updatedStories);
        })
        .catch(error => {
            console.error('Error deleting story:', error);
        });
    };


    const handleEdit = (storyId) => {
        fetch(`/story/${storyId}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                mon_name: newName,
                origin_story: newOg_story,
                L_book: newBook
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to update story');
            }
            return response.json();
        })
        .then(updatedStory => {
            const updatedStories = change.map(story =>
                story.id === storyId ? updatedStory : story
            );
            setChange(updatedStories);
            setEditingStory(null); // Close the form
        })
        .catch(error => {
            console.error('Error updating story:', error);
        });
    };

    const startEditing = (story) => {
        setEditingStory(story.id);
        setNewName(story.mon_name);
        setNewOg_story(story.origin_story);
        setNewBook(story.L_book);
    };





   
    return(
        <>
         <div>
            <ul>
                {change.map(story => (
                    <li key={story.id}>
                        {story.mon_name}
                        <button onClick={() => startEditing(story)}>Edit</button>
                    </li>
                ))}
            </ul>
            {editingStory && (
                <div>
                    <h3>Edit Story</h3>
                    <form
                        onSubmit={(e) => {
                            e.preventDefault();
                            handleEdit(editingStory);
                        }}
                    >
                        <div>
                            <label>
                                Name:
                                <input type="text" value={newName} onChange={(e) => setNewName(e.target.value)}/>
                            </label>
                        </div>
                        <div>
                            <label>
                                Origin Story:
                                <input type="text" value={newOg_story} onChange={(e) => setNewOg_story(e.target.value)}/>
                            </label>
                        </div>
                        <div>
                            <label>
                                Book:
                                <input type="text" value={newBook} onChange={(e) => setNewBook(e.target.value)}/>
                            </label>
                        </div>
                        <button type="submit">Update</button>
                        <button type="button" onClick={() => setEditingStory(null)}>Cancel</button>
                    </form>
                </div>
            )}
        </div>
        <div>
            <ul>
                {change.map(story => (
                    <li key={story.id}>
                        <Label value={story.mon_name} />
                        <button onClick={() => deleteStory(story.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
         <form onSubmit={addStory}>
            <Label value="Monster's Name" />
        <TextInput value={name} onChange={(e) => setName(e.target.value)} type='text' id="name"/>
          <Label value="Origin Story" />
        <TextInput value={og_story} onChange={(e) => setOg_story(e.target.value)} type='text' id="og_story"/>
        <Label value="Information about how their species is in Monster high" />
        <TextInput value={book} onChange={(e) => setBook(e.target.value)} type='text' id="book"/>
      <Button variant='primary' className='mt-3' type="submit">Add your the pieces of brain to the jar of this webiste</Button>
    </form>
        </>
    );
}

export default Change