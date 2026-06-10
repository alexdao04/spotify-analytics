# Things we might want to consider as this project progresses:

**Stage 1: aggregate our user data**
- This is in the form of a static website that integrates with the Spotify Web API. This should give us the target data we need
- This will require Alex (the person writing this) to create a spotify dev account and figure out a place to store this raw user data

**Stage 2: Clean the data (this is Jack's domain):**
- Rules & Conventions
Missing days: If a participant did not listen at all on a given day, omit that row entirely — do not insert a row of nulls.
Minimum threshold: Only include days where track_count >= 3. Days with fewer than 3 tracks are too sparse to be meaningful and should be dropped.
Timestamps: No raw timestamps in the final file. All time information has been converted to date, day_of_week, and the ratio columns above.
Participant IDs: Use user_01 through user_N. The mapping between real Spotify usernames and these IDs lives in a separate private file that never gets committed to GitHub.
Audio features: All features are track-level values from the Spotify audio features endpoint, aggregated to daily means. Standard deviation columns are included for valence and energy only — add others if modeling reveals they're useful.
Session definition: A new session begins when the gap between two consecutive tracks exceeds 30 minutes. This threshold can be adjusted but must be consistent across all participants.


**Stage 3: Compare models**
- Compare different classifier models to see which fit our data best and have the strongest evidence for trends by individual feature as well as when aggregated in data visualization. 
    - we won’t think about this until later when we have our data
