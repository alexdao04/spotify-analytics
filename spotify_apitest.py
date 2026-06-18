import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import json
load_dotenv() # pass by reference for my env file 

# API CONNECTION TEST CASES.
# first test: establish basic connection to spotify API
def test_spotify_connection():
    # spotipy will do the heavy lifting for oauth
    sp = spotipy.Spotify(
        auth_manager = SpotifyOAuth(
            client_id = os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret = os.getenv('SPOTIFY_CLIENT_SECRET'),
            # i'm guessing this is where our api creds go
            redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI'), 
            # i'm guessing this is for the uri to redirect to after you're done?
            scope='user-library-read') # look at user's tracks
            )
    
    # we're testing the connection to the API to start
    if sp is not None:
        print("Connection was established.")
        return True
    # else:
    print("Connection failed.")
    return False

def test_user_data_request():
    artist_uri = None # hasn't been assigned yet
    
    if __name__ == "__main__":
        test_spotify_connection()
