import React from 'react';
import EpisodeData from './EpisodeData';
const Body = () => {
    return (
        <div>
            <EpisodeData />
        </div>
    );
};

const styles = {
    main: {
        padding: '1rem',
        background: '#f4f4f4',
    },
    title: {
        fontSize: '1.5rem',
        fontWeight: 'bold',
    },
    description: {
        fontSize: '1rem',
        color: '#666',
    },
};

export default Body;
