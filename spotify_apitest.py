import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from datetime import datetime

# what we want to test first:
# first: establish basic connection to spotify API

def test_spotify_connection():
    # spotipy will do the heavy lifting
    sp = spotipy.Spotify(authmanager = SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                    client_secret='YOUR_CLIENT_SECRET',
                                                    redirect_uri='YOUR_REDIRECT_URI',
                                                    scope='user-library-read'))
    
    # this gets the current user's saved tracks?
    # we're testing the connection to the API to start
    if(sp.current_user_saved_tracks(True)):
        print("Connection to Spotify API successful!")
        
    else:
        print("Failed to connect to Spotify API.")
        assert False

