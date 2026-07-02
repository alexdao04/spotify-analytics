import os
from dotenv import load_dotenv, find_dotenv
from flask import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler

load_dotenv(find_dotenv())


class CredentialsManager:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

    @classmethod
    def build_client_credentials_spotify(cls):
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

        if not client_id or not client_secret:
            raise ValueError('SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set.')

        credentials_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret,
        )

        return spotipy.Spotify(client_credentials_manager=credentials_manager)

    @classmethod
    def build_user_oauth_spotify(cls):
        client_id = os.getenv('SPOTIFY_CLIENT_ID')
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

        if not (client_id and client_secret and redirect_uri):
            raise ValueError('SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, and SPOTIFY_REDIRECT_URI must be set.')

        auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope='user-read-private user-read-email user-read-recently-played',
            cache_handler=CacheFileHandler(cache_path='spotify_token_cache')
        )

        return spotipy.Spotify(auth_manager=auth_manager)

    @staticmethod
    def get_recently_played(sp, limit=10):
        return sp.current_user_recently_played(limit=limit)
    

    @staticmethod
    def aggregate_listening_data(sp, recently_played):
        items = []
        for item in recently_played.get('items', []):
            track = item.get('track', {})
            items.append({
                'track_name': track.get('name'),
                'artist': track.get('artists', [{}])[0].get('name'),
                'track_id': track.get('id'),
            })
        return items


def get_recently_played(sp, limit=10):
    return CredentialsManager.get_recently_played(sp, limit=limit)


def get_audio_features(sp, track_ids):
    return CredentialsManager.get_audio_features(sp, track_ids)


def aggregate_listening_data(sp, recently_played):
    return CredentialsManager.aggregate_listening_data(sp, recently_played)


if __name__ == '__main__':
    manager = CredentialsManager()
    sp = manager.build_user_oauth_spotify()
    recent = manager.get_recently_played(sp)
    print(json.dumps(recent, indent=2))
