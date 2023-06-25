line=input().split()

res=int(line[0])
for i in range(1,len(line)):
    res*=int(line[i])
print(res)