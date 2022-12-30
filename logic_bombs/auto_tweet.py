from youtubesearchpython import *
import random
import tweepy
import time
import os
import re
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()


# Replace these with your own Twitter API credentials
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

# Authenticate with the Twitter API using your API credentials
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set the time when the tweet should be sent
tweet_time = datetime(year=2022, month=12, day=23, hour=11, minute=11, second=0)

channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
id=channelsSearch.result()['result'][0]["id"]

playlist = Playlist(playlist_from_channel_id(id))
pl=playlist.info["info"]["link"]
videos=Playlist.getVideos(pl)
ch=random.randint(0,9)
vid_link = videos["videos"][ch]["link"]
github_link = 'https://github.com/Sanjin84/pylinux/blob/main/logic_bombs/auto_tweet.py'
my_tweet = ''' Hi I am Sanjin's bot and I am alive! Check out this video from my master's channel: {}

you can read my code here GitHub link:{}
'''.format(vid_link,github_link)


while True:
    # Check the current time
    current_time = datetime.now()
    print(current_time)
    # If the current time is equal to the tweet time, send the tweet
    if current_time > tweet_time:
        #api.update_status("Hello World My Bot is Alive!")
        print(my_tweet)
        # Set the tweet time to the next day at 8AM
        tweet_time = tweet_time + timedelta(days=1)
        print('I just tweeted')
    # Sleep for 1 minute before checking the time again
    time.sleep(60)
