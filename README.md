# spotify-analytics
Jack Rudy, Alexander Dao
06/09/2026

Documentation adapted from original Google Docs write up. - AD

**Spotify Day-of-Week Classifier**
Project Outline & Team Guidelines:
Can we predict the day of the week from Spotify listening patterns alone?

1. Research Question
Can a machine learning classifier predict the day of the week (Mon–Sun) based solely on a person's Spotify listening behavior that day — including the audio features of songs played and how long they listened?
This is a 7-class classification problem with clean, measurable inputs and clear evaluation metrics. No mood surveys, no self-reported data — just behavioral signals from the API.

2. Why This Works as a Project
End-to-end pipeline from API auth to trained model to deployed demo — every stage is portfolio-worthy
Clean ML framing: defined inputs, defined outputs, standard evaluation (accuracy, F1, confusion matrix)
No mood data overhead, which eliminates the biggest logistical risk from similar projects
Interesting finding either way: high accuracy means people have detectable weekly rhythms; low accuracy means listening is more random than assumed — both are reportable results
Shareable artifact: a Streamlit app or GitHub Pages write-up is easy to link on a resume or LinkedIn

3. Data
What you're collecting
Recently played tracks via the Spotify Web API
Audio features per track: valence, energy, tempo, danceability, acousticness, loudness, instrumentalness, speechiness
Session-level aggregates you compute: total listen time per day, track count, unique artist count
Day-of-week label derived from the track timestamp — this is your target variable (y)
How to get it
Each participant authenticates via Spotify OAuth (the programmer builds this flow)
Use the "Get Recently Played Tracks" endpoint with automated daily pulls
Alternative: participants download their full Spotify data dump from Privacy Settings — no API needed, covers 12 months
Legality & consent
Spotify's API Terms of Service allow personal, non-commercial use
Have every participant sign a simple one-paragraph consent form stating what data is collected and how it's used
Store data locally or in a private GitHub repo — never push raw personal listening data to a public repo
How much data do you need
Target 5–10 participants, minimum 8 weeks of listening history per person
More participants = stronger generalization; more weeks = better class balance across weekdays
Weekend days are often underrepresented in recent history — the full data dump option helps here

4. Technical Stack
Programmer / Data Engineer
Python: requests or spotipy library for API calls
OAuth 2.0: Authorization Code Flow (Spotify's standard flow for user data)
Storage: SQLite or flat CSV files per participant
Automation: cron job or GitHub Actions for daily pulls during collection window
Delivery: Streamlit for the final interactive demo
Data Scientist / Analyst
pandas + numpy for cleaning and feature engineering
scikit-learn for model training (Random Forest, Logistic Regression, optionally XGBoost)
matplotlib / seaborn for visualizations (confusion matrix, feature importance)
Jupyter Notebooks for exploratory analysis and model iteration

5. ML Approach
Feature vector (per day per person)
Mean and standard deviation of: valence, energy, tempo, danceability, acousticness, loudness
Total tracks played, total listen time in minutes, unique artist count
Time-of-day distribution: proportion of listening in morning / afternoon / evening / night
Model selection
Start with Random Forest — handles mixed feature types well and gives feature importance for free
Baseline comparisons: Logistic Regression and a majority-class dummy classifier
Optional stretch: XGBoost or a simple neural net if time permits
Evaluation
Train/test split: 80/20, stratified by day of week to ensure class balance
Primary metric: macro-averaged F1 score (more honest than accuracy for 7-class problems)
Visualization: 7×7 confusion matrix — usually the most interesting output
Baseline to beat: 1/7 = 14.3% random chance; aim for >35% to show meaningful signal
Honest framing If accuracy is low, that's not a failure — it means listening behavior doesn't strongly encode day-of-week patterns, which is itself a finding worth reporting. The write-up should discuss what features were most informative and what that implies about behavior.

6. Team Roles & Collaboration
The project splits cleanly along a data handoff boundary. The programmer owns the pipeline from API to clean dataset; the data scientist owns everything from clean dataset to findings.
Programmer / Data Engineer
Spotify Developer app registration and OAuth flow
Automated daily data collection pipeline
Raw data storage and schema design
Clean, merged dataset delivery (one row per participant per day)
Final demo deployment via Streamlit or GitHub Pages
Data Scientist / Analyst
Feature engineering from raw audio features
Exploratory data analysis (EDA)
Model training, evaluation, and iteration
Visualizations and findings write-up
Interpretation: what does the model tell us about listening behavior?
Shared
GitHub repo management and code review
Participant recruitment and consent
Final README and presentation

7. 8-Week Timeline
Week
Phase
Alex
Jack
1–2
Setup
Register Spotify Developer app, implement OAuth flow for all participants, test API token refresh
Define features list, set up shared GitHub repo, document schema expectations
3–4
Collection
Build pipeline: pull recently-played tracks + audio features daily, store as CSV, schedule automated pulls
Validate raw data, spot-check for errors, begin EDA on early data, draft cleaning logic
5
Cleaning
Deliver clean merged dataset — one row per participant per day with day-of-week label
Feature engineering: aggregate daily audio features (mean, std, session count, listen time), confirm class balance
6–7
Modeling
Assist with model integration, maintain reproducible train/test split scripts, version control notebooks
Train baseline classifier, evaluate with F1 + confusion matrix, iterate with feature importance analysis
8
Polish
Build Streamlit dashboard or GitHub Pages write-up
Write findings narrative, generate final visualizations, interpret results


8. Key Considerations & Risks
Data risks
Small N problem: with fewer than 5 participants the model may overfit to individual habits — recruit at least 6–8 people
Class imbalance: weekdays will likely have more observations than weekends — use stratified splitting and macro F1
Sparse days: some participants may not listen on certain days — decide upfront whether to drop those rows or impute
Methodological considerations
Individual variation is expected and interesting: some people have strong day patterns, others don't — report per-person accuracy separately
Don't overstate results: this is a small-N behavioral study, not a generalizable population finding — frame it that way
Feature leakage check: make sure no features accidentally encode the day (e.g. timestamp components left in)
Resume & portfolio framing
Lead with the pipeline, not just the model — API integration + OAuth + automated collection is impressive engineering work
The confusion matrix is your hero visualization: immediately readable and shows nuance a single accuracy number doesn't
Write a clean README: explain the question, the method, and the finding in three paragraphs — recruiters read these
Even a simple Streamlit demo that lets you select a participant and see their predictions is far more impressive than a notebook

9. Final Deliverables
Private GitHub repo with clean, documented code and a public-facing README
Jupyter notebook covering EDA, model training, and evaluation
Streamlit app or static GitHub Pages write-up with interactive confusion matrix
One-page summary of findings suitable for a portfolio or sending to recruiters

Estimated total project time: 6–8 weeks — resume-ready artifact at the end

