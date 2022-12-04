import gdown, sys



url = sys.argv[1]
if url.split('/')[-1] == '?usp=sharing':
  url= url.replace('?usp=sharing','')
	
gdown.download_folder(url)

