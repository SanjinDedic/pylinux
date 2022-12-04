import gdown, sys

url = sys.argv[1]

file_id = url.split('/')[-2]

prefix = 'https://drive.google.com/uc?/export=download&id='

gdown.download(prefix+file_id)
