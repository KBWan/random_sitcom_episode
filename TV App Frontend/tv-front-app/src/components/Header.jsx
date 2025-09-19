import React from 'react';

const Header = () => {
    return (
        <header style={styles.header}>
            <h1 style={styles.title}>Random Sitcom Episode</h1>
        </header>
    );
};

const styles = {
    header: {
        background: '#222',
        color: '#fff',
        padding: '16px 32px',
        textAlign: 'center',
    },
    title: {
        margin: 0,
        fontSize: '2rem',
        fontWeight: 'bold',
    },
};

export default Header;