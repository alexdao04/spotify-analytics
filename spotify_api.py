import os
import unittest
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Load environment variables from .env if present.
load_dotenv(find_dotenv())


def build_client_credentials_spotify():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    if not client_id or not client_secret:
        raise ValueError('SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set for Spotify API integration tests.')

    credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret,
    )

    return spotipy.Spotify(client_credentials_manager=credentials_manager)


def build_user_oauth_spotify():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

    if not (client_id and client_secret and redirect_uri):
        raise ValueError('SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI must be set for user-scoped Spotify tests.')

    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope='user-read-private',
    )

    return spotipy.Spotify(auth_manager=auth_manager)

if __name__ == "__main__":
    build_client_credentials_spotify()
    build_user_oauth_spotify()