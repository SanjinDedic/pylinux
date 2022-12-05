#this script integrated downloading files and folders
#it also incluses a -help

import urllib.request,os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gitfile', '--download_github_file', help="Downloads a Github File")
    parser.add_argument('-gitfolder', '--download_github_folder', help="Downloads a Github Folder")
    
    args = parser.parse_args()

    if args.download_github_file:
        url = args.download_github_file
        url = url.replace("/blob","")
        url = url.replace("github.com","raw.githubusercontent.com")
        file_name = url.split('/')[-1]
        urllib.request.urlretrieve(url, file_name)
        print("File downloaded")

    if args.download_github_folder:
        os.system('gitdir '+args.download_github_folder)
        print("Folder downloaded")

if __name__=="__main__":
    main()