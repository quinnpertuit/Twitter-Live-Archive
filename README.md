# Twitter Live Archive

1. Script `twitter_live_archive.py` 
    - Runs continuously.
    - Checks every 3 seconds for new tweets by a user.
    - If a new tweet is found, saves the twitter api json output locally.
    - Submits the tweet url to the wayback machine archiver.


2. Script `process_cancel_culture.py`
    - Processes output from [[cancel-culture]](https://github.com/travisbrown/cancel-culture) archive fetcher.
