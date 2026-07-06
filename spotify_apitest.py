import os
import unittest
import json
from dotenv import load_dotenv, find_dotenv
from spotify_api import CredentialsManager


load_dotenv(find_dotenv())


class TestSpotifyApiIntegration(unittest.TestCase):
    def test_spotify_public_api_connection(self):
        try:
            sp = CredentialsManager.build_client_credentials_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        result = sp.search(q='Shoreline Mafia', type='artist', limit=10)
        self.assertIsInstance(result, dict)
        self.assertIn('artists', result)
        self.assertIsInstance(result['artists'], dict)
        self.assertGreater(len(result['artists'].get('items', [])), 0)
        print("Public API Test Result:\n", result)


    def test_spotify_user_profile_connection(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        user = sp.current_user()
        self.assertIsInstance(user, dict)
        self.assertIn('id', user)
        self.assertTrue(user['id'])
    

    def test_get_recently_played(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=10)
        self.assertIsInstance(recently_played, dict)
        self.assertIn('items', recently_played)
        self.assertGreater(len(recently_played['items']), 0)
        
        print("\n=== Recently Played Tracks ===")
        for item in recently_played['items']:
            track = item['track']
            print(f"  {track['name']} by {track['artists'][0]['name']}")
        print("\n")


    def test_aggregate_listening_data(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=10)
        items = CredentialsManager.aggregate_listening_data(sp, recently_played)
        
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)
        
        print("\n=== Aggregated Listening Data ===\n")
        print(json.dumps(items[:2], indent=2), "\n\n... (showing first of", len(items), "items)\n")


if __name__ == '__main__':
    unittest.main()
