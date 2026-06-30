# spotify-analytics
Jack Rudy, Alexander Dao<br>
06/09/2026<br>

Documentation adapted from original Google Docs write up. - AD<br>

**Spotify Day-of-Week Classifier**<br>
Project Outline & Team Guidelines:<br>
Can we predict the day of the week from Spotify listening patterns alone?

1. Research Question<br>
Can a machine learning classifier predict the day of the week (Mon–Sun) based solely on a person's Spotify listening behavior that day — including the audio features of songs played and how long they listened?<br>
This is a 7-class classification problem with clean, measurable inputs and clear evaluation metrics. No mood surveys, no self-reported data — just behavioral signals from the API.<br>

2. What and Why<br>
Our target: End-to-end pipeline from API auth to trained model to deployed demo.
Clean ML framing: defined inputs, defined outputs, standard evaluation (accuracy, F1, confusion matrix)<br>
No mood data overhead, which eliminates the biggest logistical risk from similar projects<br>
Interesting finding either way: high accuracy means people have detectable weekly rhythms; low accuracy means listening is more random than assumed — both are reportable results<br>
<br>

3. Data<br>
What you're collecting:<br>
Recently played tracks via the Spotify Web API<br>
Audio features per track: valence, energy, tempo, danceability, acousticness, loudness, instrumentalness, speechiness<br>
Session-level aggregates you compute: total listen time per day, track count, unique artist count<br>
Day-of-week label derived from the track timestamp — this is your target variable (y)<br>
How to get it:<br>
Each participant authenticates via Spotify OAuth (the programmer builds this flow)<br>
Use the "Get Recently Played Tracks" endpoint with automated daily pulls<br>
Alternative: participants download their full Spotify data dump from Privacy Settings — no API needed, covers 12 months
Legality & consent<br>
Spotify's API Terms of Service allow personal, non-commercial use<br>
Have every participant sign a simple one-paragraph consent form stating what data is collected and how it's used<br>
Store data locally or in a private GitHub repo — never push raw personal listening data to a public repo<br>
How much data do you need?<br>
Target 5–10 participants, minimum 8 weeks of listening history per person<br>
More participants = stronger generalization; more weeks = better class balance across weekdays<br>
Weekend days are often underrepresented in recent history — the full data dump option helps here<br>

4. Technical Stack<br>
Programmer / Data Engineer<br>
Python: requests or spotipy library for API calls<br>
OAuth 2.0: Authorization Code Flow (Spotify's standard flow for user data)<br>
Storage: SQLite or flat CSV files per participant<br>
Automation: cron job or GitHub Actions for daily pulls during collection window<br>
Delivery: Streamlit for the final interactive demo
Data Scientist / Analyst<br>
pandas + numpy for cleaning and feature engineering
scikit-learn for model training (Random Forest, Logistic Regression, optionally XGBoost)<br>
matplotlib / seaborn for visualizations (confusion matrix, feature importance)<br>
Jupyter Notebooks for exploratory analysis and model iteration<br>

5. ML Approach<br>
Feature vector (per day per person)<br>
Mean and standard deviation of: valence, energy, tempo, danceability, acousticness, loudness<br>
Total tracks played, total listen time in minutes, unique artist count<br>
Time-of-day distribution: proportion of listening in morning / afternoon / evening / night<br>
Model selection:<br>
Start with Random Forest — handles mixed feature types well and gives feature importance for free<br>
Baseline comparisons: Logistic Regression and a majority-class dummy classifier<br>
Optional stretch: XGBoost or a simple neural net if time permits<br>
Evaluation:<br>
Train/test split: 80/20, stratified by day of week to ensure class balance<br>
Primary metric: macro-averaged F1 score (more honest than accuracy for 7-class problems)<br>
Visualization: 7×7 confusion matrix — usually the most interesting output<br>
Baseline to beat: 1/7 = 14.3% random chance; aim for >35% to show meaningful signal<br>
Honest framing:<br>
If accuracy is low, that's not a failure — it means listening behavior doesn't strongly encode day-of-week patterns, which is itself a finding worth reporting. The write-up should discuss what features were most informative and what that implies about behavior.<br>

6. Team Roles & Collaboration<br>
The project splits cleanly along a data handoff boundary. The programmer owns the pipeline from API to clean dataset; the data scientist owns everything from clean dataset to findings.<br>
Programmer / Data Engineer<br>
Spotify Developer app registration and OAuth flow<br>
Automated daily data collection pipeline<br>
Raw data storage and schema design<br>
Clean, merged dataset delivery (one row per participant per day)<br>
Final demo deployment via Streamlit or GitHub Pages<br>
Data Scientist / Analyst<br>
Feature engineering from raw audio features<br>
Exploratory data analysis (EDA)<br>
Model training, evaluation, and iteration<br>
Visualizations and findings write-up<br>
Interpretation: what does the model tell us about listening behavior?<br>
Shared<br>
GitHub repo management and code review<br>
Participant recruitment and consent<br>
Final README and presentation<br>

7. 8-Week Timeline<br>
Week 1–2<br>
Setup<br>
Register Spotify Developer app, implement OAuth flow for all participants, test API token refresh<br>
Define features list, set up shared GitHub repo, document schema expectations<br>
3–4<br>
Collection<br>
Build pipeline: pull recently-played tracks + audio features daily, store as CSV, schedule automated pulls
Validate raw data, spot-check for errors, begin EDA on early data, draft cleaning logic<br>
5<br>
Cleaning<br>
Deliver clean merged dataset — one row per participant per day with day-of-week label<br>
Feature engineering: aggregate daily audio features (mean, std, session count, listen time), confirm class balance
6–7<br>
Modeling<br>
Assist with model integration, maintain reproducible train/test split scripts, version control notebooks<br>
Train baseline classifier, evaluate with F1 + confusion matrix, iterate with feature importance analysis<br>
8<br>
Polish<br>
Build Streamlit dashboard or GitHub Pages write-up<br>
Write findings narrative, generate final visualizations, interpret results<br>


8. Key Considerations & Risks<br>
Data risks<br>
Small N problem: with fewer than 5 participants the model may overfit to individual habits — recruit at least 6–8 people<br>
Class imbalance: weekdays will likely have more observations than weekends — use stratified splitting and macro F1<br>
Sparse days: some participants may not listen on certain days — decide upfront whether to drop those rows or impute
Methodological considerations<br>
Individual variation is expected and interesting: some people have strong day patterns, others don't — report per-person accuracy separately<br>
Don't overstate results: this is a small-N behavioral study, not a generalizable population finding — frame it that way<br>
Feature leakage check: make sure no features accidentally encode the day (e.g. timestamp components left in)
Resume & portfolio framing<br>
Lead with the pipeline, not just the model — API integration + OAuth + automated collection is impressive engineering work<br>
The confusion matrix is your hero visualization: immediately readable and shows nuance a single accuracy number doesn't<br>

9. Final Deliverables<br>
Jupyter notebook covering EDA, model training, and evaluation<br>
Streamlit app or static GitHub Pages write-up with interactive confusion matrix<br>
<br>
Estimated total project time: 6–8 weeks — resume-ready artifact at the end<br>

