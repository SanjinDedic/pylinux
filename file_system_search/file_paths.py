import os
from pptx import Presentation
import re
from openpyxl import load_workbook
import time
from docx import Document
from pathlib import Path
from time import sleep
directory =r"G:\My Drive\Head Start Academy\Scripts\Github data\pylinux\file_system_search\FILE_JUNGLE"
totalsize=0
def logsize(root,file):
    global totalsize
    size=os.path.getsize(os.path.join(root, file))
    totalsize+=size
    print("{f} | {size} | Bytes".format(f=file,size=size))
    

[(logsize(root,file)) for root, dirs, files in os.walk(directory) for file in files if file.endswith((".txt",".pdf",".xlsx",".pptx",".docx")) ]
print("{size:.2f} MB".format(size=totalsize/(1024**3)))
"""
directory =r"G:\My Drive\Head Start Academy\Scripts\Github data\pylinux\file_system_search\FILE_JUNGLE"
counter=0
def check(root,file):
    global counter
    if file.endswith(".txt"):
        file_path=os.path.join(root, file)
        data=''
        txt = Path(file_path).read_text()
        #data = txt.replace('\n', '')
        result=re.findall("AAA",txt)
        if  result:
            return print(result[0]+" in file"+file)

#[print(os.path.join(root, file)) for root, dirs, files in os.walk(directory) for file in files ]
[check(root,file) for root, dirs, files in os.walk(directory) for file in files if file.endswith((".txt",".pdf",".xlsx",".pptx",".docx")) ]#map(str.upper,os.walk(directory))
#file_path=os.path.join(root, file)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
"""