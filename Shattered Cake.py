W=int(input())
N=int(input())
A=0

for i in range(N):
    wl=input().split()
    w=int(wl[0])
    l = int(wl[1])
    a=w*l
    A+=a
print(A//W)

