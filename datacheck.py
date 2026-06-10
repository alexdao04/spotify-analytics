# this will have checks/tests to ensure that the data we have is valid before we start cleaning or analyzing it

import sqlite3

def check_recently_played_data(db_path='spotify_data.db'):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Check if recently_played table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='recently_played'")
    if not c.fetchone():
        print("Error: recently_played table does not exist.")
        return False
    
    # Check for null values in critical columns
    c.execute("SELECT COUNT(*) FROM recently_played WHERE track_id IS NULL OR track_name IS NULL OR artist_name IS NULL")
    null_count = c.fetchone()[0]
    if null_count > 0:
        print(f"Warning: Found {null_count} records with null values in critical columns.")
    
    # Check for duplicate entries (same user, track, and played_at)
    c.execute("""
        SELECT user_spotify_id, track_id, played_at, COUNT(*)
        FROM recently_played
        GROUP BY user_spotify_id, track_id, played_at
        HAVING COUNT(*) > 1
    """)
    duplicates = c.fetchall()
    if duplicates:
        print(f"Warning: Found {len(duplicates)} duplicate records in recently_played.")
    
    print("Data check completed.")
    return True