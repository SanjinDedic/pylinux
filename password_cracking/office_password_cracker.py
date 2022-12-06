#This script will attempt each password from .txt file
#It will take an office file as a parameter and brute force attempt each password
import msoffcrypto,sys


filename=sys.argv[1].rsplit('.',1)[0] #rsplit is reverse split ,1 splits once only!
filetype=sys.argv[1].rsplit('.',1)[1]

office_types=["docx","pptx","xlsx"]
all_passwords=[]

with open("passwords.txt", "r") as f: #You can use rb for binary to get bytes in return
    lines=f.readlines()
    for line in lines: 
        all_passwords.append(line.rstrip()) #Use line.rstrip().decode() to convert bytes into strings

if filetype in office_types:
    with open(sys.argv[1], "rb") as f:
            for this_pass in all_passwords:
                try:
                    file = msoffcrypto.OfficeFile(f)
                    file.load_key(password=this_pass,verify_password=True)  # Use password                   
                    print("File Opened successfully with "+this_pass)
                    break
                except:
                    print("Incorrect Password")
else:
    print("File is not a office file")
