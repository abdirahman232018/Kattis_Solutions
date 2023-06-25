T=input()
per="PER"
days=0
t=0
while t<len(T):


    j=0
    while j<3:
        if per[j]!=T[t+j]:
            days+=1


        j+=1

    t+=3

print(days)