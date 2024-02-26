import React, { useEffect, useState } from 'react';
import Playlists from './Playlists';

const Dashboard = () => {
    const [userData, setUserData] = useState({
        username:"",
        playlists:[],
    });

    useEffect(() => {
        fetch('http://localhost:5000/dashboard')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setUserData({
                    username: data.username,
                    playlists: data.playlists,
                });
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }, []);

    return (
        <div>
            {userData && (
                <div>
                    <h1>Hello, {userData.username}!</h1>
                    {<Playlists playlists={userData.playlists} />}
                </div>
            )}
        </div>
    );
};

export default Dashboard;
