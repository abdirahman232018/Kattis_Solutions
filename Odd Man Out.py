N=int(input())
case="Case #"
for i in range(1,N+1):
    num_G=int(input())
    G=list(map(int,input().split()))
    for n in G:
        if G.count(n)==1:
            print(case+str(i)+": "+str(n))
            break

