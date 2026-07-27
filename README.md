# Spotify Day-of-Week Classifier

**Contributors:** Alexander Dao and Jack Rudy

**Started:** July 1, 2026

This project investigates whether a classifier can predict the day of the week on which a person listened to a song, using only their Spotify listening behavior.

For the current roadmap, see [progress.md](progress.md). For installation requirements, see [requirements.txt](requirements.txt).

## Data

### Target data

- Recently played tracks from the Spotify Web API
- Track audio features: valence, energy, tempo, danceability, acousticness, loudness, instrumentalness, and speechiness
- Daily listening aggregates: total listening time, track count, and unique artist count
- A day-of-week label derived from each track timestamp (so we know what songs people listen to on X day)

### Data collection

- You authenticate on Spotify's website through Spotipy, using credentials in `.env`.
- Spotify redirects to Spotipy's temporary local callback server at `http://127.0.0.1:8888/callback`.
- The collector retrieves your most recently played tracks (in its current iteration).
- Each collection is written as a timestamped raw JSON file in `data/raw/user_XX/`.
- Each user ID must use the anonymous format `user_01`, `user_02`, and so on.

### Consent and use

Spotify's API Terms of Service permit personal, non-commercial use. Each participant will be provided a short consent statement describing the data collected and its intended use. The current local workflow does not collect consent automatically; record it separately before running the collector for a participant. A future hosted service will provide the consent and data-submission flow.

### Sample size

- We plan to recruit 5–10 participants with substantial or regular listening histories.
- The more participants we have, the more patterns we'll see.

## Tech Stack

### Data engineering

- **Python:** `requests` or `spotipy` for API requests
- **Authentication:** OAuth 2.0 Authorization Code Flow
- **Storage:** Google Sheets for initial small-scale data collection

### Data science and analysis

- `pandas` and `numpy` for cleaning and feature engineering
- `scikit-learn` for model training and evaluation
- `matplotlib` and `seaborn` for visualizations, including confusion matrices and feature importance

## Machine Learning Approach

### Features

- Means and standard deviations of audio features, including valence, energy, tempo, danceability, acousticness, and loudness
- Total tracks played, total listening time in minutes, and unique artist count
- Time-of-day proportions for morning, afternoon, evening, and night

### Candidate models

- Random Forest classifier as the initial model
- Logistic Regression baseline
- Majority-class dummy classifier baseline
- XGBoost
- Neural network

## Team Roles

### Programmer / Data Engineer — Alexander Dao

- Register and configure the Spotify Developer app and OAuth flow
- Develop the future hosted participant consent and collection flow
- Automate the data-collection pipeline
- Write collected data in a usable format for analysis

### Data Scientist / Analyst — Jack Rudy

- Determine features from raw audio data
- Perform exploratory data analysis (EDA)
- Train, evaluate, and iterate on models
- Create visualizations and write up findings
- Interpret what the models reveal about listening behavior

## Environment Setup

1. Create a virtual environment (recommended):

   ```bash
   python -m venv <env_name>
   ```

2. Activate it:

   ```bash
   # macOS/Linux
   source venv/bin/activate

   # Windows
   venv\\Scripts\\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to your own `.env` file (this is for API authentication purposes), then add your Spotify credentials:

   ```dotenv
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```

5. The Spotify integration tests are meant to confirm that everything's set up correctly.
   They are to be used after configuring your credentials and redirect URI:

   ```bash
   python3 test_spotify_api.py
   ```

6. Run the JSON-writing test to authenticate with Spotify, retrieve up to 50 recently played tracks, and verify that the saved JSON can be read back:

   ```bash
   python3 test_datawrite.py
   ```

   This creates a timestamped JSON file in `data/raw/<insert_user_here>/`.

7. Collect data for an anonymous participant:

   ```bash
   python3 -m backend.datawrite --user-id <insert_user_here>
   ```

   Spotipy opens Spotify's authorization website in your browser. After approval,
   Spotify redirects to the local callback, and the collector saves a timestamped
   response in `data/raw/<insert_user_here>/`. The participant's OAuth token is cached in
   `.spotify_tokens/<insert_user_here>.json`.

## Current Workflow

```text
.env credentials
       ↓
CredentialsManager creates a Spotify OAuth client
       ↓
Spotify returns recently played tracks
       ↓
DataWriter saves a timestamped raw JSON response
       ↓
data/raw/user_XX/<timestamp>-recently-played.json
```

The current workflow is local and CLI-based. GitHub Pages cannot run the Python
collector or write files to a researcher's computer. A future participant-facing
version will require a hosted backend, a production OAuth callback, explicit
consent, and private storage.

## Project Layout

```text
backend/                 CredentialsManager and DataWriter classes
frontend/                Informational GitHub Pages site
data/raw/user_XX/        Timestamped participant JSON output (not committed)
.spotify_tokens/         Per-participant OAuth token caches (not committed)
test_datawrite.py        Live fetch, save, and JSON-readback test
test_spotify_api.py      Additional Spotify integration tests
```
