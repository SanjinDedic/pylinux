#go to a channel get a video url for a random pick of the last 10 videos given a channel
from youtubesearchpython import *
import random
import tweepy
import time
from datetime import datetime, timedelta

# Replace these with your own Twitter API credentials
api_key = "AECmDmtQfqPfNMv81D0isbA2K"
api_secret = "14QOgZHCGojVvxz5G1erkusNRIODdBmI8zjC3mIXpYDCgzUxAz"
access_token = "255962528-fL707Q4XJIVipUG0h6T7tfVFPVFMtXaEDpqunUDD"
access_token_secret = "YkpPFbCP4TltyhAwzJZjTnugw0Bj2vcdPeeZLB6neRSfo"

# Authenticate with the Twitter API using your API credentials
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Set the time when the tweet should be sent
tweet_time = datetime(year=2022, month=12, day=24, hour=13, minute=38, second=0)

channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
id=channelsSearch.result()['result'][0]["id"] 

playlist = Playlist(playlist_from_channel_id(id))
print(playlist)
pl=playlist.info["info"]["link"]
print(pl)
videos=Playlist.getVideos(pl)
print(videos)
ch=random.randint(0,9)
vid_link = videos["videos"][ch]["link"]
skinny_link = vid_link.split('&list')[0]


github_link = 'https://github.com/Sanjin84/pylinux/blob/main/logic_bombs/auto_tweet.py'
my_tweet = ''' Hi I am Sanjin's bot and I am alive! Below is my random video selection for today from Sanjin's channel:

Take a look at my GitHub code here:{}

{}
'''.format(github_link, skinny_link)
'''
while True:
    # Check the current time
    current_time = datetime.now()
    print(current_time)
    # If the current time is equal to the tweet time, send the tweet
    if current_time > tweet_time:
        print(my_tweet)
        api.update_status(my_tweet)
        # Set the tweet time to the next day at 8AM
        tweet_time = tweet_time + timedelta(days=1)
        print('I just tweeted')
    # Sleep for 1 minute before checking the time again
    time.sleep(60)

'''