# PlaylistPilot

This is PlaylistPilot! 
A  web application that leverages a content-based recommendation system to provide users with song recommendations based on their Spotify playlists

## Motivation
During my Information Retrieval class, I learned about various recommendation systems, sparking my curiosity about their real-world applications. As a frequent Spotify user who enjoys curating playlists based on different genres, moods, and seasons, I've always wondered about the algorithms behind Spotify's song recommendations. To delve deeper into this, I created PlaylistPilot, a project aimed at exploring and potentially improving the song recommendations provided by Spotify. 

## 🚀 Quick Start
Clone the repo to run locally:
Install the depedencies
* Node.js and npm 
* React
* Flask, Flask-CORS
* Python

Start the backend/server
```bash
cd backend
python3 app.py
```
Start the frontend/client
```bash
cd frontend
npm i
npm run start
```

## Usage

1. **Sign In**: Users begin by signing into PlaylistPilot using their Spotify account credentials. This ensures that the app can access their playlists and track features to generate personalized recommendations
2. **Playlist Selection**: Upon signing in, users are presented with a list of their created playlists. They can choose a playlist they wish to see new song recommendations
3. **Recommedations**: After selecting a playlist, PlaylistPilot generates a list of the top 5 songs to recommend for that specific playlist. These recommednations are based on various factors including the playlist's genre, mood, and audio features.
    * **Feature Representation:**
    Represented each song in the dataset as a vector of popularity, genre, and audio features which include: danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, temp, duration_ms, and time_signature
    * **User Profile:**
    Created a user profile based on the songs in the user's playlist. Aggreate the same features on the songs in the playlist (popularity, genre(s), and auido features) to represent the user's preferences.
    * **Similarity Calculation:**
    Used cosine similarity to calcualte the similarity between each song in the dataset and the uesr profile

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
