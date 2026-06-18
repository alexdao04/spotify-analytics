import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from datetime import datetime

def spotify_api_handler(): # this 
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            redirect_uri='YOUR_REDIRECT_URI',
            scope='user-library-read')
            )

    if sp is not None:
        print("Connection was established.")
        return True
    # else:
    print("Connection failed.")
    return False
    # we know this part works

if __name__ == "__main__":
    spotify_api_handler()