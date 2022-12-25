#works for all file types (pdf docx xlxs pptx rar zip)https://github.com/Sanjin84/pylinux
#if password list not given, the script will ask if you want to download and use rockyou.txt

import os
import sys
import urllib
import pathlib
try: #trys importanting non pre-packaged libraries
	import pikepdf
	import msoffcrypto
	import argparse
	import wget
except ModuleNotFoundError: #if user did not previously install libraries will install for them
	install = input("Requirments not found on computer, would you like to install them automatically? Y/N\n>>> ")
	if install.lower() == ('y'):
		os.system("pip install pikepdf")
		os.system("pip install msoffcrypto-tool")
		os.system("pip install argparse")
		os.system("pip install wget")
	#Retry Imports Once Libraries Are Installed
	import pikepdf
	import msoffcrypto
	import argparse
	import wget


#Setting up arguments for command line
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name', help="Enter the file path")
parser.add_argument('-p', '--pass_list', help="Enter the password list path")
args = parser.parse_args()

#Getting users download path
downloads_path = str(pathlib.Path.home() / "Downloads")

#Saving given password list to all_passwords
all_passwords=[]

valid_pass = True

if args.pass_list is None: # if no password list argument was passed (args.passlist is None)
	valid_pass=False
	if os.path.exists(downloads_path + "/rockyou.txt"): # checks if file exists (~/Downloads/rockyou.txt)
		useExisting = input('rockyou.txt file found in Downloads. Would you like to use this file? Y/N\n>>> ')
		if useExisting.lower() == 'y':
			args.pass_list = downloads_path + "/rockyou.txt"
			valid_pass = True
	if valid_pass == False: # if rockyou.txt was not found
		install = input("No passwords list added, would you like to download common password list rockyou.txt? Y/N\n>>> ")
		if install.lower() == "y":
			try:
				if os.path.exists(downloads_path + "/rockyou.txt"): # if rockyou.txt exists but user does not want to use it
					args.pass_list = downloads_path + "/rockyou.txt.1"
				else: # if rockyou.txt exists
					args.pass_list = downloads_path + "/rockyou.txt"
				#url = 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'
				os.system('cd ~/Downloads && wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt') # change directory to downloads before downloading rockyou.txt
				print("rockyou.txt Download: Success!\nrockyou.txt downloaded to ~/Downloads/rockyou.txt")
				valid_pass = True
			except urllib.error.URLError: # Error when not having internet
				print("rockyou.txt Download: Failed.\nMaybe you dont have internet connection?")
				valid_pass = False

if valid_pass == False: # if no pass_list was added
	print("Exiting...")
	sys.exit()
	
	
try: # trys to open in 'read mode'
	with open(args.pass_list, "r") as f: #You can use rb for binary to get bytes in return
		lines=f.readlines()
		for line in lines: 
			all_passwords.append(line.rstrip()) #Use line.rstrip().decode() to convert bytes into strings
except UnicodeDecodeError: # opens in 'read binary mode'
	with open(args.pass_list, "rb") as f: #You can use rb for binary to get bytes in return
		lines=f.readlines()
		for line in lines: 
			all_passwords.append(line.rstrip()) #Use line.rstrip().decode() to convert bytes into strings


#Checking if the password given is correct or not
if args.file_name.endswith(("docx","pptx","xlsx")):
    with open(args.file_name, "rb") as f:
            for this_pass in all_passwords:
                try:
                    this_pass = str(this_pass, 'utf-8') # convert binary to utf-8
                except:
                    pass
                try:
                    file = msoffcrypto.OfficeFile(f)
                    file.load_key(password=this_pass,verify_password=True)  # Use password                   
                    print("File Opened With: "+this_pass)
                    break
                except:
                    print("Incorrect Password: "+this_pass)

elif args.file_name.endswith(".pdf"):
    for one_pass in all_passwords:
        try:
            one_pass = str(one_pass, 'utf-8') # convert binary to utf-8
        except:
            pass
        try:
            with pikepdf.open(args.file_name, password=one_pass) as pdf:
            	print('File Opened With: '+one_pass)
            	break 
        except:
            print("Incorrect Password: "+one_pass)
         
else: # file extension is not docx, pptx, xlsx or pdf
    print("File is not appropiate")
