import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from datetime import datetime

def spotify_api_handler():
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='user-library-read')
            )
