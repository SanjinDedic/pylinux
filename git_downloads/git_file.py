import urllib.request, sys 

url = sys.argv[1]
url = url.replace("/blob","")
url = url.replace("github.com","raw.githubusercontent.com")
file_name = url.split('/')[-1]
urllib.request.urlretrieve(url, file_name)
