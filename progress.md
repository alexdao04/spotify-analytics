# Project Progress

**Maintainer:** Alexander Dao

**Last updated:** July 26, 2026

## Stage 1: Collect User Data — In Progress

- [x] Create an informational static website for the project.
- [x] Build the local Python Spotify OAuth flow.
- [x] Retrieve a user's recently played tracks through the CLI.
- [x] Save timestamped raw JSON responses in `data/raw/user_XX/`.
- [x] Verify a saved JSON response can be read back in `tests/test_datawrite.py`.
- [ ] Build and deploy a participant-facing consent and data-collection service.
- [ ] Decide on private shared storage for finalized participant data.

The current collector is intentionally local. Spotipy opens Spotify's authorization
website, receives the callback at `http://127.0.0.1:8888/callback`, and uses a
separate token cache for each `user_XX` ID. Participant data and token caches are
ignored by Git.

The GitHub Pages site is informational only. It does not authenticate participants
or communicate with the Python collector. A future hosted service will own the
public OAuth callback, consent flow, and private data submission.

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
