import json
import unittest
from dotenv import load_dotenv, find_dotenv

from backend import CredentialsManager, DataWriter


load_dotenv(find_dotenv())


class TestWrite(unittest.TestCase):
    def test_valid_json_response(self):
        try:
            sp = CredentialsManager.build_user_oauth_spotify()
        except ValueError as exc:
            self.skipTest(str(exc))

        recently_played = CredentialsManager.get_recently_played(sp, limit=50)
        # for the purposes of this test we just want the most recent tracks
        self.assertIsInstance(recently_played, dict)
        # make sure that our recently played is in a dictionary format
        # meaning no data corruption
        self.assertIn('items', recently_played)
        # check for items element in the first place
        self.assertGreater(len(recently_played['items']), 0)
        # and whether theres any items in there (len > 0)


        output_file = DataWriter.save_recently_played("user_01", recently_played)
        self.assertTrue(output_file.exists())
        try:
            with output_file.open(encoding="utf-8") as file:
                self.assertEqual(json.load(file), recently_played)
            print(f"\n✓ Saved and verified recently played data: {output_file}")
        except Exception as err:
            self.fail(f"Failed to read or parse the saved JSON file: {err}")



if __name__ == '__main__':
    unittest.main(verbosity=2)
