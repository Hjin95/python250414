#demoOS.py
from os.path import *

#print(dir())
print(abspath("python.exe"))
print(basename("c:\\work\\python.exe"))

fileName=r"c:\python310\python.exe"

if exists(fileName):
    print("파일의 크기:",getsize(fileName))
else:
    print("파일없음")

#운영체제 정보
import os
print("운영체제 이름 : ",os.name)
print("환경변수 :",os.environ)
#os.system("notepad.exe") < 주석풀면 메모장실행

#파일리스트
import glob
print("---파일리스트---")
print(glob.glob(r"c:\work\*.py"))

for item in glob.glob(r"c:\work\*.py"):
    print(item)