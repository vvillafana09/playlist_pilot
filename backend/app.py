from flask import Flask, redirect, request, session, url_for, jsonify, json, session
from flask_cors import CORS
from spotify_api import get_auth_manager, get_sp, current_user_info, get_user_playlists, current_playlist_tracks, playlist_track_recommedation
import os

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    auth_manager = get_auth_manager()
    auth_url = auth_manager.get_authorize_url()
    return {'redirect_url': auth_url}

@app.route('/callback', methods=['POST'])
def callback():
    code = request.get_json().get('code')
    auth_manager = get_auth_manager()
    token_info = auth_manager.get_access_token(code, as_dict=False)
    session['token_info'] = token_info
    return redirect(url_for("dashboard"))

@app.route('/dashboard', methods=['GET'])
def dashboard(): 
    auth_manager = get_auth_manager()
    sp = get_sp(auth_manager)
    user_info = current_user_info(sp)
    user_id = user_info['id']
    user_name = user_info['display_name']
    playlists = get_user_playlists(sp, user_id)
    return {
        'username': user_name,
        'playlists': playlists
    }

@app.route('/dashboard/<id>', methods=['GET', 'POST'])
def songs(id):
    auth_manager = get_auth_manager()
    sp = get_sp(auth_manager)
    playlist_track_info, tracks_from_playlist = current_playlist_tracks(sp, id)
    songs_recommended = playlist_track_recommedation(sp, tracks_from_playlist)
    return {
        'playlist_songs': playlist_track_info,
        'recommended_songs': songs_recommended
    }
    

if __name__ == '__main__':
    app.run(debug=True)