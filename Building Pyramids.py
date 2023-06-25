N=int(input())
h=0
blocks_used=0
sq=1
while True:
    s=sq*sq
    if s+blocks_used<=N:
        h+=1
        blocks_used+=s
        sq+=2
    else:
        break
print(h)


