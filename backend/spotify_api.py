import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
from recommendation import recommend_songs

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

def get_auth_manager():
    return SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-library-read', cache_path='.spotify_cache')

def get_sp(auth_manager):
    return spotipy.Spotify(auth_manager=auth_manager)

# get the current user's id
def current_user_info(spotify_sp):
    current_user = spotify_sp.current_user()
    return current_user

# get the playlist(s) name and id from user
def get_user_playlists(spotify_sp, user_id):
    playlist_info = []
    playlists = spotify_sp.user_playlists(user_id)
    i = 0
    for playlist in playlists['items']:
        i += 1
        playlist_data = {
            "name": playlist['name'],
            "playlist_id": playlist['id'],
            "id": i
        }
        playlist_info.append(playlist_data)
    return playlist_info

# get the tracks based on a single playlist 
def current_playlist_tracks(spotify_sp, playlist_id):
    results = spotify_sp.playlist_tracks(playlist_id)
    tracks_from_playlist = results['items']
    playlist_tracks_info = []
    i = 0
    # Loop through each track in the playlist
    for track in tracks_from_playlist:
        i += 1
        # Extract the track information
        artist_name = track['track']['album']['artists'][0]['name']
        track_name = track['track']['name']
        duration_ms = track['track']['duration_ms']
        album_name = track['track']['album']['name']
        
        # Create a dictionary to store the track information
        track_info = {
            'artist_name': artist_name,
            'track_name': track_name,
            'duration_ms': duration_ms,
            'album_name': album_name,
            'id': i
        }
        
        # Add the track information to the list
        playlist_tracks_info.append(track_info)
    return playlist_tracks_info, tracks_from_playlist

# extract the tracks audio features for calculations
def playlist_track_recommedation(spotify_sp, tracks):
    track_data = []
    for track in tracks:
        track_id = track['track']['id']
        artist_id = track['track']['artists'][0]['id']
        popularity = track['track']['popularity']

        features = spotify_sp.audio_features([track_id])[0]

        artist = spotify_sp.artist(artist_id)
        genres = artist['genres']

        data = {
            'track_id': track_id,
            'duration_ms': features['duration_ms'],
            'danceability': features['danceability'],
            'energy': features['energy'],
            'key': features['key'],
            'loudness': features['loudness'],
            'mode': features['mode'], 
            'speechiness': features['speechiness'],
            'acousticness': features['acousticness'],
            'instrumentalness': features['instrumentalness'],
            'liveness': features['liveness'],
            'valence': features['valence'],
            'tempo': features['tempo'],
            'time_signature': features['time_signature'],
            'genres': genres,
            'popularity': popularity
        }

        track_data.append(data)
    songs_to_recommend = recommend_songs(track_data, "dataset.csv")
    recommend_info_songs = [
        {
            'id': index,
            'track_name': row['track_name'],
            'artists': row['artists'],
            'album_name': row['album_name'],
            'duration_ms': row['duration_ms']
        }
        for index, row in songs_to_recommend.iterrows()
    ]
    return recommend_info_songs
