import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from datetime import datetime

# TEST CASES FOR API CONNECTION FOR PULLING RAW DATA
# first test: establish basic connection to spotify API

def test_spotify_connection():
    # spotipy will do the heavy lifting
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='user-library-read')
            )
    
    # this gets the current user's saved tracks?
    # we're testing the connection to the API to start
    if sp is not None:
        print("Connection was established.")
        return True
    # else:
    print("Connection failed.")
    return False
    
if __name__ == "__main__":
    test_spotify_connection()