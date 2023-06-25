line=input()
n=len(line)

i=0
while i<=n:
    if i+2<=n and (line[i:i+2]==":)" or line[i:i+2]==";)"):
        print(i)
    elif i+3<=n and (line[i:i+3]==";-)" or line[i:i+3]==":-)"):
        print(i)
    i+=1