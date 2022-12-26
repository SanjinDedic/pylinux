from youtubesearchpython import *

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