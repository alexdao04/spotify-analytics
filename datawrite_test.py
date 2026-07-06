# local test for later

import json
import unittest
from dotenv import load_dotenv, find_dotenv
from spotify_api import CredentialsManager

class TestWrite(unittest.TestCase):
    def test_write_recently_played_to_json(self):
        load_dotenv(find_dotenv())
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=10)
        # for the purposes of this test we just want the most recent tracks
        self.assertIsInstance(recently_played, dict)
        # make sure that our recently played is in a dictionary format
        # meaning no data corruption
        self.assertIn('items', recently_played)
        # check for items element in the first place
        self.assertGreater(len(recently_played['items']), 0)
        # and whether theres any items in there (len > 0)


        # Write to JSON file
        with open('user-data.json', 'w') as f:
            json.dump(recently_played, f, indent=4)

        print("Recently played tracks written to user-data.json")
