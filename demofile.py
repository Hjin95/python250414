# demofile.py

f=open("c:\\work\\test.txt","wt", encoding="utf-8")
f.write("첫번쨰\n두번째\n세번째\n")
f.close()

#읽기
f=open(r"c:\\work\\test.txt","rt", encoding="utf-8")
result=f.read()
print(result)
f.close()
