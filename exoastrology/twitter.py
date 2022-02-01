import tweepy
import os
import time
import emoji

from datetime import datetime, timedelta

from .util import split_string

from pathlib import Path
from .horoscope import generate, generate_initial_tweet


def _read_keys_file(file_location=None):
    """Reads the keys file, which should be five keys on five lines in the order of:
    bearer_token, consumer_key, consumer_secret, access_token, access_token_secret
    """

    if file_location is None:
        file_location = Path(os.getenv("TWITTER_KEYS"))

    with open(file_location) as handle:
        result = handle.read().splitlines()

    return result


def start_client(file_location=None, wait_on_rate_limit=True):
    """Starts the Twitter client!"""
    return tweepy.Client(*_read_keys_file(file_location), wait_on_rate_limit=wait_on_rate_limit)


def post_thread(client, string, tweet_to_reply_to=None):
    """Posts a thread to twitter dot com"""
    # Convert any emojis
    string = emoji.emojize(string, use_aliases=True)

    # Format the string to not be terrible
    tweets = split_string(string)

    for i, a_tweet in enumerate(tweets):
        try:
            # Todo: handle
            response = client.create_tweet(in_reply_to_tweet_id=tweet_to_reply_to, text=a_tweet)
            tweet_to_reply_to = response[0]['id']

        except tweepy.TweepyException as e:
            # Todo: clever exception handling if it isn't an issue-exception
            raise e

        # A little bit of slight rate limiting if we're posting a thread
        if i + 1 < len(tweets):
            time.sleep(30)

    return tweet_to_reply_to


def post_horoscope(client, interval=120):
    """Posts the horoscope for a day!"""
    # Send the initial tweet
    print("Posting initial tweet!")
    id = post_thread(client, generate_initial_tweet())
    print("  sent!")

    for i in range(12):
        time.sleep(interval)

        print(f"posting horoscope {i+1}!")
        id = post_thread(client, generate(i), tweet_to_reply_to=id)
        print("  sent!")

    print("All done! \o/")


def run_horoscopes(at=11, immediately=False, file_location=None, interval=120):
    """Run the client stuff and post horoscopes routinely!"""
    print("Starting client!")

    # Initiate Tweepy client
    client = start_client(file_location=file_location)

    # Calculate first run time (only case when we could post same-day)
    now = datetime.now()

    if immediately:
        print("Posting a delayed horoscope at next opportunity!")
        next_run = now
    elif now.hour < at:
        next_run = datetime(year=now.year, month=now.month, day=now.day, hour=at)
    else:
        next_run = datetime(year=now.year, month=now.month, day=now.day, hour=at) + timedelta(days=1)

    # Main loop
    while True:

        # Sleep!
        seconds_to_sleep = (next_run - now).total_seconds()

        if seconds_to_sleep > 0.0:
            print(f"Sleeping for {seconds_to_sleep / 60**2:.2f} hours...")
            time.sleep(seconds_to_sleep)

        # Post the horoscope
        post_horoscope(client, interval=interval)

        # Calculate next runtime
        now = datetime.now()
        next_run = datetime(year=now.year, month=now.month, day=now.day + 1, hour=at)
