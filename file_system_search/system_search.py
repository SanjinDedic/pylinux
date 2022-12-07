#This script goes through every sub folder from an identified folder
#It searches for a string within popular document types: office, pdf, archives
#It can also search via built in linux commands like find

import sys,os,re
from PyPDF2 import PdfFileReader
from openpyxl import load_workbook
from pptx import Presentation
from docx import Document


directory = r"{}".format(sys.argv[1])
text = sys.argv[2]


for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".txt"):
            file_path=os.path.join(root, file)
            with open(file_path, 'r') as f:
                print(re.findall(text,f.read()))
                break
        
        if file.endswith(".pdf"):
            file_path=os.path.join(root, file)
            with open(file_path, 'rb') as f:
                pdf_file=PdfFileReader(f)
                data=''
                for i in range(pdf_file.numPages):
                    page = pdf_file.getPage(i)
                    data += page.extractText()
                print(re.findall(text,data))
                break
                
        if file.endswith(".xlsx"):
            file_path=os.path.join(root, file)
            data=''
            wb = load_workbook(file_path)
            all_rows = list(wb.rows)

            for cell in all_rows[0]:
                data+=cell.value
            print(re.findall(text,data))
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
                print(re.findall(text,data))
                break
        
        if file.endswith(".docx"):
            file_path=os.path.join(root, file)
            data=''
            with open(file_path, 'rb') as f:
                doc = Document(file)
                data=''
                for para in doc.paragraphs:
                    data += '\n'+ para.text
                print(re.findall(text,data))
                break