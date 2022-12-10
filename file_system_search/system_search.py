#This script goes through every sub folder from an identified folder
#It searches for a string within popular document types: office, pdf, archives
#It can also search via built in linux commands like find

import sys,os,re
from PyPDF2 import PdfFileReader
from openpyxl import load_workbook
from pptx import Presentation
from docx import Document
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('-path', '--source_path', help="Takes the directory path in quotes as input")
#parser.add_argument('-t', '--text_pattern', help="Takes the text pattern as input")

#rgs = parser.parse_args()

directory = sys.argv[1]#args.source_path
text = sys.argv[2]+".+}"#args.text_pattern+".+}" #Has the text with one or more characters and ends with }


for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".txt"):
            file_path=os.path.join(root, file)
            data=''
            with open(file_path, 'r') as f:
                data+=f.read()
                result=re.findall(text,data)
                if not result:
                    continue
                else:
                    print(result[0])
                    break    
            
        if file.endswith(".pdf"):
            file_path=os.path.join(root, file)
            with open(file_path, 'rb') as f:
                pdf_file=PdfFileReader(f)
                data=''
                for i in range(pdf_file.numPages):
                    page = pdf_file.getPage(i)
                    data += page.extractText()
                result=re.findall(text,data)
                if not result:
                    continue
                else:
                    print(result[0])
                    break 
                
        if file.endswith(".xlsx"):
            file_path=os.path.join(root, file)
            data=''
            wb = load_workbook(file_path)
            ws = wb.active
            for row in ws:
                for cell in row:
                    if cell.value is not None:
                        data+=str(cell.value)
            result=re.findall(text,data)
            if not result:
                    continue
            else:
                print(result[0])
                break         

        if file.endswith(".pptx"):
            file_path=os.path.join(root, file)
            data=''
            with open(file_path, 'rb') as f:
                prs = Presentation(f)
                for slide in prs.slides:
                    for shape in slide.shapes:
                        if hasattr(shape, "text"):
                            data=shape.text
                result=re.findall(text,data)
                if not result:
                    continue
                else:
                    print(result[0])
                    break 
        
        if file.endswith(".docx"):
            file_path=os.path.join(root, file)
            data=''
            with open(file_path, 'rb') as f:
                doc = Document(file)
                data=''
                for para in doc.paragraphs:
                    data += '\n'+ para.text
                result=re.findall(text,data)
                if not result:
                    continue
                else:
                    print(result[0])
                    break 