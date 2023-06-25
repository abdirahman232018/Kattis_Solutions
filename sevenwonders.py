
cards=input()
n=len(cards)
t,c,g=0,0,0


for i in range(n):

    if cards[i]=="T":
        t+=1
    elif cards[i]=="C":
        c+=1
    elif cards[i]=="G":
        g+=1

total_points=(t*t)+(c*c)+(g*g)
total_sets=(min(t,c,g))*7
print(total_points+total_sets)

