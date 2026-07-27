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

- A local user authenticates through Spotify OAuth using credentials in `.env`.
- The collector retrieves up to 50 recently played tracks per run.
- Each collection is written as a timestamped raw JSON file in `data/raw/user_XX/`.
- Each user ID must use the anonymous format `user_01`, `user_02`, and so on.

### Consent and use

Spotify's API Terms of Service permit personal, non-commercial use. Each participant should provide a short consent statement describing the data collected and its intended use. The GitHub Pages frontend will collect this consent before data submission.

### Recommended sample size

- Recruit 5–10 participants with substantial or regular listening histories.
- More participants improve generalization; more weeks improve class balance across weekdays.

## Tech Stack

### Data engineering

- **Python:** `requests` or `spotipy` for API requests
- **Authentication:** OAuth 2.0 Authorization Code Flow
- **Storage:** Google Sheets for initial small-scale data collection

### Data science and analysis

- `pandas` and `numpy` for cleaning and feature engineering
- `scikit-learn` for model training and evaluation
- `matplotlib` and `seaborn` for visualizations, including confusion matrices and feature importance
- Jupyter notebooks for exploratory analysis and model iteration

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

### Evaluation

- Use an 80/20 train/test split stratified by day of week.
- Use macro-averaged F1 score as the primary metric.

High accuracy would suggest detectable weekly listening rhythms. Low accuracy is also a useful result: it may show that listening behavior does not strongly encode day-of-week patterns.

## Team Roles

### Programmer / Data Engineer — Alexander Dao

- Register and configure the Spotify Developer app and OAuth flow
- Integrate the GitHub Pages demo with the Spotify API
- Automate the data-collection pipeline
- Write collected data in a usable format for analysis

### Data Scientist / Analyst — Jack Rudy

- Determine features from raw audio data
- Perform exploratory data analysis (EDA)
- Train, evaluate, and iterate on models
- Create visualizations and write up findings
- Interpret what the models reveal about listening behavior

### Shared responsibilities

- Hold periodic pair reviews or weekly check-ins
- Recruit participants and collect consent

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

4. Copy `.env.example` to `.env`, then add your Spotify credentials:

   ```dotenv
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```

5. Run the JSON-writing test to authenticate with Spotify, retrieve up to 50 recently played tracks, and verify that the saved JSON can be read back:

   ```bash
   python3 test_datawrite.py
   ```

   This creates a timestamped JSON file in `data/raw/user_01/`.

6. To collect data directly, provide an anonymous participant ID:

   ```bash
   python3 -m backend.datawrite --user-id user_01
   ```

   An OAuth token cache is created at `.spotify_cache/user_01.json`. Use a different `user_XX` ID for each participant.

7. The Spotify integration tests are meant to confirm that everything's set up correctly. 
   They are to be used after configuring your credentials and redirect URI:
   ```bash
   RUN_SPOTIFY_INTEGRATION=1 python3 test_spotify_api.py
   ```

8. When you're ready, integrate your account credentials once you've set up your own access tokens. Go to:
   ```
   [Integration](https://alexdao04.github.io/spotify-analytics/frontend/index.html)
   ```

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

The current workflow is local and CLI-based. The frontend is a separate GitHub Pages OAuth prototype; it is not yet connected to the Python JSON collector.

## Project Layout

```text
backend/                 CredentialsManager and DataWriter classes
frontend/                GitHub Pages OAuth prototype (not connected to backend)
data/raw/user_XX/        Timestamped participant JSON output (not committed)
test_datawrite.py        Live fetch, save, and JSON-readback test
test_spotify_api.py      Additional Spotify integration tests
```
