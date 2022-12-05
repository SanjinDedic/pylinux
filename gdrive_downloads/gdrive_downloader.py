#this script will download files and folders from google drive
#It will perform some basic url cleaning to work with different types of links
#The users will also have access to a help function

import wget,gdown
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-gfile', '--download_google_file', help="Downloads a Google File")
    parser.add_argument('-gfolder', '--download_google_folder', help="Downloads a Google Folder")
    
    args = parser.parse_args()

    if args.download_google_file:
        url = args.download_google_file
        file_id = url.split('/')[-2]

        prefix = 'https://drive.google.com/uc?/export=download&id='
        wget.download(prefix+file_id)
        print("File downloaded")

    if args.download_google_folder:
        url = args.download_google_folder
        if url.split('/')[-1] == '?usp=sharing':
            url= url.replace('?usp=sharing','')
        gdown.download_folder(url)
        print("Folder downloaded")


if __name__=="__main__":
    main()