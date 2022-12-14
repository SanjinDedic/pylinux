#works for all file types (pdf docx xlxs pptx rar zip)https://github.com/Sanjin84/pylinux
#if password list not given, the script will ask if you want to download and use rockyou.txt
from PyPDF2 import PdfFileReader
import msoffcrypto
import argparse

#Setting up arguments for command line
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name', help="Enter the file path")
parser.add_argument('-p', '--pass_list', help="Enter the password list path")
args = parser.parse_args()

#Saving given password list to all_passwords
all_passwords=[]

with open(args.pass_list, "r") as f: #You can use rb for binary to get bytes in return
    lines=f.readlines()
    for line in lines: 
        all_passwords.append(line.rstrip()) #Use line.rstrip().decode() to convert bytes into strings

#Checking if the password given is correct or not
if args.file_name.endswith(("docx","pptx","xlsx")):
    with open(args.file_name, "rb") as f:
            for this_pass in all_passwords:
                try:
                    file = msoffcrypto.OfficeFile(f)
                    file.load_key(password=this_pass,verify_password=True)  # Use password                   
                    print("File Opened successfully with "+this_pass)
                    break
                except:
                    print("Incorrect Password")

elif args.file_name.endswith(".pdf"):
    for one_pass in all_passwords:
        try:
            file = PdfFileReader(args.file_name,password=one_pass)
            print("File Opened successfully with "+one_pass)
            break
        except:
            print("Incorrect Password")
else:
    print("File is not appropiate")
