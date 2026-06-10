from flask import Flask, redirect, request, jsonify
from spotify_api import SpotifyDataCollector
import os

# handles http requests/routing 
# acts as a point of contact for front and back end
# from our end device to spotify's servers and back

app = Flask(__name__)

collector = SpotifyDataCollector(
    client_id=os.getenv('SPOTIFY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
    redirect_uri='http://localhost:5000/callback' # 
)

@app.route('/login')
def login():
    auth_url = collector.sp.auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    collector.sp.auth_manager.get_access_token(request.args['code'])
    count = collector.sync_user(None)
    return jsonify({'synced': count})

@app.route('/api/status')
def status():
    return jsonify({'ready': True})

if __name__ == '__main__':
    app.run(debug=True)