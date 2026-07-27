import json
import unittest

from backend.spotify_api import CredentialsManager


class TestSpotifyApiIntegration(unittest.TestCase):
    def test_public_search_returns_artist_results(self):
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


    def test_authorized_user_profile_has_an_id(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        user = sp.current_user()
        self.assertIsInstance(user, dict)
        self.assertIn('id', user)
        self.assertTrue(user['id'])
    

    def test_recently_played_response_contains_tracks(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=50)
        self.assertIsInstance(recently_played, dict)
        self.assertIn('items', recently_played)
        self.assertGreater(len(recently_played['items']), 0)
        
        print("\n=== Recently Played Tracks ===")
        for item in recently_played['items']:
            track = item['track']
            print(f"  {track['name']} by {track['artists'][0]['name']}")
        print("\n")


    def test_aggregation_extracts_track_fields(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=50)
        items = CredentialsManager.aggregate_listening_data(recently_played)
        
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)
        
        print("\n=== Aggregated Listening Data ===\n")
        print(json.dumps(items[:2], indent=2), "\n\n... (showing first of", len(items), "items)\n")


if __name__ == '__main__':
    unittest.main(verbosity=2)
