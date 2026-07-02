**Spotify Day-of-Week Classifier Project**<br>
Alexander Dao<br>
Jack Rudy<br>
July 1, 2026<br>

General overview of the what and why behind this project.<br>
For more information on how we're planning this project. see "progress.md".<br>

1. The What<br>
Can a machine learning classifier predict songs listened to on a given day of the week, based solely on a person's Spotify listening behavior?<br>

2. Data<br>
Target Data:<br>
- Recently played tracks via the Spotify Web API<br>
- Audio features per track: valence, energy, tempo, danceability, acousticness, loudness, instrumentalness, speechiness<br>
- Session-level aggregates you compute: total listen time per day, track count, unique artist count<br>
- Day-of-week label derived from the track timestamp — this is your target variable (y)<br>
Target Data Acquisition:<br>
- Each participant authenticates via Spotify OAuth.<br>
- Aggregate listening data once OAuth handshake is completed.<br>
Legality & consent<br>
- Spotify's API Terms of Service allow personal, non-commercial use<br>
- Have every participant sign a simple one-paragraph consent form stating what data is collected and how it's used.<br>
- This consent form will be done on the GitHub Pages front end, where users submit their Spotify account data.<br>
- Data will be stored in a private-access Google Sheet.<br>
How much data do you need?<br>
- Target 5–10 participants, ideally those with significant listening history or semi-regular use<br>
- More participants = stronger generalization; more weeks = better class balance across weekdays<br>

3. What we're gonna use (tech stack)<br>
Programmer / Data Engineer<br>
Python: requests or spotipy library for API calls<br>
OAuth 2.0: Authorization Code Flow (Spotify's standard flow for user data)<br>
Storage: Probably Google Sheets for simplicity later on. This project doesn't have AWS money, man!<br>
(will be retroactively updated as needed)<br>
Data Scientist / Analyst<br>
pandas + numpy for cleaning and feature engineering<br>
scikit-learn for model training (Random Forest, Logistic Regression, optionally XGBoost)<br>
matplotlib / seaborn for visualizations (confusion matrix, feature importance)<br>
Jupyter Notebooks for exploratory analysis and model iteration<br>

4. ML Approach<br>
Features to watch:<br>
- Mean and STDev of features (e.g. valence, energy, tempo, danceability, acousticness, loudness)<br>
- Total tracks played, total listen time in minutes, unique artist count<br>
- Time-of-day distribution: proportion of listening in morning / afternoon / evening / night<br>

Model selection:<br>
- We could start with random forests — handles mixed feature types well.<br>
- Other models for baseline comparison: 
    - Logistic Regression<br>
    - Majority-class dummy classifier<br>
    - XGNet<br>
    - Neural<br>

Evaluation:<br>
- Train/test split: 80/20, stratified by day of week to ensure class balance<br>
- Primary metric: macro-averaged F1 score<br>

Results:<br>
- High accuracy means people have detectable weekly rhythms.<br>
- Low accuracy means listening is more random than assumed — both are reportable results.<br>
- If accuracy is low, that's not a failure — it means listening behavior doesn't strongly encode day-of-week patterns, which is itself a finding worth reporting.<br>
5. Team Roles & Collaboration<br>
Programmer / Data Engineer (Alexander Dao)<br>
Responsibilities included:<br>
- Spotify Developer app registration and OAuth flow<br>
- API integration with Demo via GitHub Pages<br>
- Automating the data collection pipeline<br>
- Ensuring data is written to our initial collection file in proper format, so that the data scientist working on this doesn't want to kill me.<br>
Data Scientist / Analyst (Jack Rudy)<br>
Responsibilities included:<br>
- Feature engineering from raw audio features<br>
- Exploratory data analysis (EDA)<br>
- Model training, evaluation, and iteration<br>
- Visualizations and findings write-up<br>
- Interpretation (what does the model tell us about listening behavior?)<br>
Shared Responsibilities:<br>
- Periodic pair review/weekly project check-in<br>
- Participant recruitment and consent<br>
