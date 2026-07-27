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
- A day-of-week label derived from each track timestamp (the target variable, `y`)

### Data collection

- Each participant authenticates through Spotify OAuth.
- Listening data is aggregated after the OAuth handshake completes.
- Data will be stored in a private-access Google Sheet.

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

- Engineer features from raw audio data
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
   python -m venv venv
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

4. Create a `.env` file next to `requirements.txt`:

   ```dotenv
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=your_redirect_uri
   ```

5. Run the API script:

   ```bash
   python spotify_api.py
   ```
