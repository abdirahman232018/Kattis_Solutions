import math
sum1=0
min1=math.inf
max1=-1

N=int(input())

for _ in range(N):
    num=int(input())
    sum1+=num
    if num<min1:
        min1=num
    if num>max1:
        max1=num
mods=[]
smallest_m=max1%min1


for i in range(smallest_m,min1,smallest_m):
    if (sum1%i)==(min1%i)*N:
        mods.append(i)
print(*mods)
