
got_away=True
blimps=[]
for i in range(1,6):
    blimp=input()
    n=len(blimp)

    for j in range(n):
        if j+2<n and blimp[j]=="F" and blimp[j+1]=="B" and blimp[j+2]=="I":
            got_away=False

            blimps.append(str(i))



if got_away:
    print("HE GOT AWAY!")
else:

    print(" ".join(blimps))
