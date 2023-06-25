T=int(input())

for _ in range(T):
    line1=input()
    line2=input()
    outpout = ""
    for i in range(len(line1)):
        if line1[i]==line2[i]:
            outpout+="."
        else:
            outpout+="*"
    print(line1)
    print(line2)
    print(outpout)

