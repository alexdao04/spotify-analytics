# Project Progress

**Maintainer:** Alexander Dao

**Last updated:** July 26, 2026

## Stage 1: Collect User Data — In Progress

- [x] Create a static website that integrates with the Spotify Web API.
- [x] Build a Python Spotify OAuth demo.
- [x] Retrieve a user's recently played tracks through the CLI.
- [x] Save timestamped raw JSON responses in `data/raw/user_XX/`.
- [x] Verify a saved JSON response can be read back in `test_datawrite.py`.
- [ ] Connect the frontend OAuth flow to the Python data collector.
- [ ] Decide on private shared storage for finalized participant data.

The current collector is local and uses a separate OAuth token cache for each `user_XX` ID. Participant data and token caches are ignored by Git.

## Stage 2: Clean the Data — Jack's Focus

### Cleaning rules

#### Missing days

If a participant did not listen on a day, omit that day entirely. Do not create a row containing null values.

#### Minimum threshold

Only include days where `track_count >= 3`. Days with fewer than three tracks are too sparse to be meaningful.

#### Timestamps

Do not include raw timestamps in the final dataset. Convert time information into `date`, `day_of_week`, and the relevant time-of-day ratio columns.

#### Participant IDs

Use IDs in the form `user_01` through `user_N`. Keep the mapping to real Spotify usernames in a separate private file that is never committed to GitHub.

#### Audio features

Aggregate track-level audio features to daily means. Include standard deviation columns for valence and energy; add others later only if modeling shows they are useful.

#### Session definition

Start a new session when the gap between consecutive tracks exceeds 30 minutes. Use this threshold consistently for every participant.

## Stage 3: Compare Models

- [ ] Compare classifier models to find the best fit for the data.
- [ ] Evaluate evidence for trends in individual features and in aggregated visualizations.
