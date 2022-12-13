# Pylinux
---

This repository will be used as a tool in the future to perform certain tasks that need more code for linux and windows. This repository find certain text searches for all common files (.docx, .xlsx, .pptx, .pdf, .txt, .zip, .rar). It also cracks encryted files by the given password list through brute force. 

# Table of Contents
1. [File system search](https://github.com/Sanjin84/pylinux/edit/main/data.md#file-system-search)
2. [File manipulation](https://github.com/Sanjin84/pylinux/edit/main/data.md#file-system-search)
3. [Download from Google drive]()
4. [Download from Github]()
5. [Password Cracking]()


# File system search
## System search
It goes through every file and unpacks if they are archived and then searches the text on the whole directory for each file. It takes two arguments. One is the file path and second is the text.
```
python system_search.py -path "the_path" -text abc
```

## Office Flag Finder
You can search any text in Word, Excel and Powerpoint file. It takes two arguments. One is the file path and second is the text.
```
python office_flag_finder.py file-path text
```

## PDF Flag Finder
You can search any text in a PDF file. It takes two arguments. One is the file path and second is the text.
```
python pdf_flag_finder.py file-path text
```

# File manipulation
