import zipfile
import sys,os,re
import patoolib  #pip install patool

file = sys.argv[1]

if file.endswith(".zip"):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(os.getcwd()+"\\extracted_zip")

if file.endswith(".rar"):
    patoolib.extract_archive(file, outdir=os.getcwd()+"\\extracted_rar")
