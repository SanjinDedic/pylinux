from youtubesearchpython import *
import re

channelsSearch = ChannelsSearch('Sanjin Dedic', limit = 1, region = 'US')
id=channelsSearch.result()['result'][0]["id"] 

playlist = Playlist(playlist_from_channel_id(id))

pl=playlist.info["info"]["link"]

videos=Playlist.getVideos(pl)
vid_link = videos["videos"][0]["link"]
skinny_link = vid_link.split('&list')[0]

vid_title = videos["videos"][0]["accessibility"]["title"]
result=re.search("\d+ hours",vid_title)

if int(result.group().split(" ")[0])<5:
    print("New video is out here and was uploaded "+result.group()+" ago"+"\n"+skinny_link)
