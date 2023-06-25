n=int(input())

bats=input()
total=0
slugs=0
for b in (bats.split()):
    b=int(b)
    if b!=-1:
        slugs+=1
        total+=b

print("%.3f"%(total/slugs))