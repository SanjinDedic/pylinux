import urllib.request, sys 

url = sys.argv[1]
file_name = url.split('/')[-1]

urllib.request.urlretrieve(url, file_name)
