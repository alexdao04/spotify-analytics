import json
import unittest
from dotenv import load_dotenv, find_dotenv
from spotify_api import CredentialsManager


load_dotenv(find_dotenv())


class TestWrite(unittest.TestCase):
    # once we've tested everything
    # we can write the recently played tracks
    pass