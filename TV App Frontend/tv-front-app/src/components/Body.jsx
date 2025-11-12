import React from 'react';
import EpisodeData from './EpisodeData';
import '../styles/Body.css';
const Body = () => {
    return (
        <div className='body-container'>
            <EpisodeData />
            <button onClick={() => window.location.reload()}>Get Another Episode</button>
        </div>
    );
};


export default Body;
