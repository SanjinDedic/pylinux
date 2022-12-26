#Open a virus scan and run it overnight if your computer is still runnig
#Open a fully legal app that downloads movies overnight
#to demo open notepad and type in HELLO.

#Only windows
import subprocess
from sys import platform

if platform == "linux" or platform == "linux2":
    subprocess.Popen(["lynis","audit","system"], shell=True, stdout=subprocess.PIPE)
elif platform == "win32":
    print(subprocess.Popen(["C:\Program Files\Windows Defender\MpCmdRun.exe","-Scan","-Scan Type","1"], shell=True, stdout=subprocess.PIPE).stdout.read())