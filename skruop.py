n=int(input())
v=7

for i in range(n):
    req=str(input())


    if req=="Skru op!" and v<10:
        v+=1

    if req=="Skru ned!" and v>0:
        v-=1


print(v)