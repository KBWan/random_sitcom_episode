import React, { useState, useEffect } from 'react';

function EpisodeData() {
    const [episode, setEpisode] = useState(null);
    const [loading, setLoading] = useState(true); // Loading state
    const [error, setError] = useState(null);     // Error state

    // Fetch episode data from python backend API
    useEffect(() => {
        // Fetch episode data from an API or local source
        fetch('http://127.0.0.1:5000/get_episode') // Replace with your actual API endpoint
            .then((response) =>{
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setEpisode(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }
    if (error) {
        return <p>Error loading episode data: {error.message}</p>;
    }

    //converts air date to more readable format
    const date = new Date(episode.air_date.year, episode.air_date.month - 1, episode.air_date.day);
    const dateOut = date.toUTCString().split(' ').slice(0, -2).join(' ');
    
    //render episode data
    return (
        <div>
            <h2>{episode.show}</h2>
            <h3>S{episode.season}E{episode.episode_number}: {episode.episode_title}</h3>
            <p>Watch Period: {episode.watch_period}</p>
            <img src={episode.image} alt={`${episode.episode_title} Poster`} style={{width: '200px'}} />
            <p>Air Date: {dateOut}</p>
            <p>IMDB Rating: {episode.rating}</p>
            <p>{episode.description}</p>
        </div>
    )
}

export default EpisodeData;