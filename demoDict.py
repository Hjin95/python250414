#demoDic.py
colors={"apple":"red","banana":"yellow"}
print(colors)
print(len(colors))
print(colors["apple"])
#입력
colors["cherry"]="red"
print(colors)

#삭제
del colors["apple"]
print(colors)

for item in colors.items():
    print(item)

#불린형식
print(1<2)
print(1!=2)
print(1==2)
print(True and True and True)
print(True and True and False)
print(True or False or False)

print(bool(0))
print(bool(3))
print(bool(None))

