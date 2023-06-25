H_M=input().split()
H=int(H_M[0])
M=int(H_M[1])

if H==0:
    mins=(24*60)-abs(M-45)
    if mins//60==24:
        print("0","00")
    else:
        print(mins//60,(mins%60))

else:
    mins=((H*60) + M)-45
    print(mins // 60,(mins % 60))




