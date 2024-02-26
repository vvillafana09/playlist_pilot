import { Link } from 'react-router-dom';

const Playlists = ({playlists}) => {
    return ( 
        <div className="playlist-list">
            {playlists.map(playlist => (
                <Link
                to={`/dashboard/${playlist.playlist_id}`}
                className="playlist-preview"
                key={playlist.id}
                >
                <h2>{playlist.name}</h2>
              </Link>
            ))}
        </div>
     );
}
 
export default Playlists;