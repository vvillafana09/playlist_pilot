import { useParams } from "react-router-dom";
import React, { useEffect, useState } from 'react';

const Songs = () => {
    const { id } = useParams();
    const [trackData, setTrackData] = useState({
        playlist_songs: [],
        recommended_songs: []
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('http://localhost:5000/dashboard/' + id)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setTrackData({
                    playlist_songs: data.playlist_songs,
                    recommended_songs: data.recommended_songs
                });
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                setLoading(false);
            });
    }, [id]);

    if (loading) return <div>Loading...</div>

    return ( 
        <div className="songs-container">
            <div className="playlist-songs">
                <h1>Playlist songs</h1>
                {trackData.playlist_songs.map(tracks => (
                    <div className="tracks-preview" key={tracks.id}>
                        <p className="song-color-change">{tracks.id}.</p>
                        <p>{tracks.track_name}</p>
                        <p className="song-color-change">{tracks.artist_name}</p>
                        <p className="song-color-change">{tracks.album_name}</p>
                    </div>
                ))}
            </div>

            <div className="recommended-songs">
                <h1>Recommended songs</h1>
                {trackData.recommended_songs.map(tracks => (
                    <div className="tracks-preview" key={tracks.id}>
                        <p>{tracks.track_name}</p>
                        <p>{tracks.artists}</p>
                        <p>{tracks.album_name}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
 
export default Songs;