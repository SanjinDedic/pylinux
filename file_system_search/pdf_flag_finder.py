from PyPDF2 import PdfFileReader
import sys,os,re

file = sys.argv[1]
text= sys.argv[2]+".+}" //".+}" . means any character + 1 or more occurences, ends with }
if file.endswith(".pdf"):
    with open(file, 'rb') as f:
        pdf_file=PdfFileReader(f)
        data=''
        for i in range(pdf_file.numPages):
            page = pdf_file.getPage(i)
            data += page.extractText()
        result=re.findall(text,data)
        print(result[0])
