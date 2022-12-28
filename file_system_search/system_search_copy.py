#This script goes through every sub folder from an identified folder
#It searches for a string within popular document types: office, pdf, archives

import os,re
from PyPDF2 import PdfFileReader
from openpyxl import load_workbook
from pptx import Presentation
from docx import Document
import argparse
from pyunpack import Archive
import shutil
import time
startTime = time.time()

#Setting up arguments for command line
parser = argparse.ArgumentParser()
parser.add_argument('-path', '--source_path', help="Takes the directory path in quotes as input")
parser.add_argument('-text', '--text_pattern', help="Takes the text pattern as input")

args = parser.parse_args()

#Assigning variables and adding regular expression for the text
directory = args.source_path
text = args.text_pattern+".+}" #Has the text with one or more characters and ends with }

def extract(root,file):
    out_zip=os.path.join(root, "extracted")
    file_path=os.path.join(root, file)
    Archive(file_path).extractall(out_zip,auto_create_dir=True)

def check(root,file):
    if file.endswith(".txt"):
            file_path=os.path.join(root, file)
            data=''
            with open(file_path, 'r') as f:
                data+=f.read()
                result=re.findall(text,data)
                if  result:
                    print(result[0]+"in file"+file)
                
    if file.endswith(".pdf"):
        file_path=os.path.join(root, file)
        pdf_file=PdfFileReader(file_path)
        data=''
        for i in range(pdf_file.numPages):
            page = pdf_file.getPage(i)
            data += page.extractText()
        result=re.findall(text,data)
        if result:
            print(result[0]+"in file"+file)
            
    if file.endswith(".xlsx"):
        file_path=os.path.join(root, file)
        data=''
        wb = load_workbook(file_path)
        ws = wb.active
        
        values=[str(cell.value) for row in ws for cell in row if cell.value is not None]
        data=' '.join(values)            
        result=re.findall(text,data)
        if result:
            print(result[0]+"in file"+file)
        
    if file.endswith(".pptx"):
        file_path=os.path.join(root, file)
        data=''
        with open(file_path, 'rb') as f:
            prs = Presentation(f)
            values=[shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")]
            data=' '.join(values)
            result=re.findall(text,data)
            if result:
                print(result[0]+" in file "+file)
            
    if file.endswith(".docx"):
        file_path=os.path.join(root, file)
        data=''
        doc = Document(file_path)
        data=''
        for para in doc.paragraphs:
            data += '\n'+ para.text
        result=re.findall(text,data)
        if result:
            print(result[0]+" in file "+file)
            
#Going through each file in the directory to unpack
[extract(root,file) for root, dirs, files in os.walk(directory) for file in files if file.endswith((".zip",".rar")) ]#map(str.upper,os.walk(directory))
#print(all_files)
[check(root,file) for root, dirs, files in os.walk(directory) for file in files if file.endswith((".txt",".pdf",".xlsx",".pptx",".docx")) ]#map(str.upper,os.walk(directory))

"""
if 'out_zip' in locals() :
    ans = input('Do you want to remove all the files that were extracted from compressed directories?   y/n?')
    if ans.lower() =='y':
        shutil.rmtree(out_zip)
        shutil.rmtree(out_rar)
"""
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))