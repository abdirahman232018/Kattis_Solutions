name=input()

name2=[]
name2.append(name[0])
for c in name:
    if name2[-1]!=c:
        name2.append(c)

print("".join(name2))