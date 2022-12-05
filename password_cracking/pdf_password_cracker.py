#This script brute forces a pdf file from a .txt password list 

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

filetype=sys.argv[1].rsplit('.',1)[1]

all_passwords=[]
with open("passwords.txt", "r") as f: #You can use rb for binary to get bytes in return
    lines=f.readlines()
    for line in lines: 
        all_passwords.append(line.rstrip()) #Use line.rstrip().decode() to convert bytes into strings

if filetype=="pdf":
    for one_pass in all_passwords:
        try:
            file = PdfFileReader(sys.argv[1],password=one_pass)
            print("File Opened successfully with "+one_pass)
            break
        except:
            print("Incorrect Password")
else:
    print("File is not a PDF")