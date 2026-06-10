import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from datetime import datetime

# oauth token management, api fetching, and database storage logic for spotify_data

class SpotifyDataCollector:
    def __init__(self, client_id, client_secret, redirect_uri, db_path='spotify_data.db'):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope='user-read-recently-played'
        ))
        
        self.conn = sqlite3.connect(db_path)
        self._init_db()
    
    def _init_db(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            spotify_id TEXT PRIMARY KEY,
            display_name TEXT,
            email TEXT,
            fetched_at TIMESTAMP
        )''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS recently_played (
            id INTEGER PRIMARY KEY,
            user_spotify_id TEXT,
            track_id TEXT,
            track_name TEXT,
            artist_name TEXT,
            played_at TIMESTAMP,
            fetched_at TIMESTAMP,
            FOREIGN KEY(user_spotify_id) REFERENCES users(spotify_id)
        )''')
        
        self.conn.commit()
    
    def sync_user(self, user_id, limit=50):
        """Fetch and store recently played for a user"""
        # Get user info
        user_info = self.sp.current_user()
        
        c = self.conn.cursor()
        c.execute('''
            INSERT OR REPLACE INTO users
            (spotify_id, display_name, email, fetched_at)
            VALUES (?, ?, ?, ?)
        ''', (
            user_info['id'],
            user_info.get('display_name'),
            user_info.get('email'),
            datetime.now().isoformat()
        ))
        
        # Get recently played
        results = self.sp.current_user_recently_played(limit=limit)
        
        for item in results['items']:
            c.execute('''
                INSERT INTO recently_played
                (user_spotify_id, track_id, track_name, artist_name, played_at, fetched_at)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                user_info['id'],
                item['track']['id'],
                item['track']['name'],
                item['track']['artists'][0]['name'],
                item['played_at'],
                datetime.now().isoformat()
            ))
        
        self.conn.commit()
        return len(results['items'])