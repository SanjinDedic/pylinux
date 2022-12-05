#This script opens a password protected pdf file
from PyPDF2 import PdfFileReader
import sys

filetype=sys.argv[1].rsplit('.',1)[1]

if filetype=="pdf":
    try:
        file = PdfFileReader(sys.argv[1],password=sys.argv[2])
        print("File Opened successfully")
    except:
        print("Incorrect Password")
else:
    print("File is not a PDF")