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


class TestSpotifyApiIntegration(unittest.TestCase):
    def test_spotify_public_api_connection(self):
        """Verify Spotify API connectivity with client credentials and a live search request."""
        try:
            sp = build_client_credentials_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        result = sp.search(q='Beatles', type='artist', limit=1)
        self.assertIsInstance(result, dict)
        self.assertIn('artists', result)
        self.assertIsInstance(result['artists'], dict)
        self.assertGreater(len(result['artists'].get('items', [])), 0)

    def test_spotify_user_profile_connection(self):
        """Verify Spotify OAuth integration by requesting the authenticated user profile."""
        try:
            sp = build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        user = sp.current_user()
        self.assertIsInstance(user, dict)
        self.assertIn('id', user)
        self.assertTrue(user['id'])


if __name__ == '__main__':
    unittest.main()
