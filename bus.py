T=int(input())


for _ in range(T):
    k=int(input())
    p=0

    while k>0:
        p+=0.5
        p*=2
        k-=1
    print(int(p))
