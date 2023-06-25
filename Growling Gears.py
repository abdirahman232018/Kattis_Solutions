
T=int(input())

for _ in range(T):
    gears=int(input())
    maxTorq0=0
    maxTorqGear=None
    for t in range(1,gears+1):
        a,b,c=list(map(int, input().split()))
        R=b/(2*a)
        curTorq=(-a*(R**2))+(b*R)+c
        if curTorq>maxTorq0:
            maxTorq0=curTorq
            maxTorqGear=t
    print(maxTorqGear)


