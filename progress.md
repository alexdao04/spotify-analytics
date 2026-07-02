Maintainer: Alexander Dao<br>
Progress document for this project. Last updated July 1, 2026.<br>

**Stage 1: aggregate our user data (mostly done)** (done)<br>
Step 1: Create a static website that integrates with the Spotify Web API. This should give us the target data we need (done).<br>
- This has been mostly done by now, now that we have a working API demo in python, we can attempt to create a flow that takes user data post-authentication and sends it straight to a private Google Sheets file (e.g. JSON).<br>
- We're not going to have to worry about rate limiting or anything seeing as this is a very small-scale project.<br>

**Stage 2: Clean the data (this is Jack's domain):**<br>
A few things to keep in mind:<br>
**Missing days**:<br>
- If a participant did not listen at all on a given day, omit that row entirely — do not insert a row of nulls.<br>
**Minimum threshold**:<br>
- Only include days where track_count >= 3. Days with fewer than 3 tracks are too sparse to be meaningful and should be dropped.<br>
**Timestamps**:<br>
- No raw timestamps in the final file. All time information has been converted to date, day_of_week, and the ratio columns above.<br>
**Participant IDs**:<br>
- Use user_01 through user_N. The mapping between real Spotify usernames and these IDs lives in a separate private file that never gets committed to GitHub.<br>
**Audio features**:<br>
- All features are track-level values from the Spotify audio features endpoint, aggregated to daily means. Standard deviation columns are included for valence and energy only — we may add others in the future if existing modeling reveals they're useful.<br>
**Session definition**:<br>
A new session begins when the gap between two consecutive tracks exceeds 30 minutes. This threshold can be adjusted but must be consistent across all participants.<br>

**Stage 3: Compare models**
- Compare different classifier models to see which fit our data best and have the strongest evidence for trends by individual feature as well as when aggregated in data visualization. 