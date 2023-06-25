import math

T=int(input())


for t in range(T):
    v,theta,x1,h1,h2=list(map(float,input().split()))

    x=float(v*t*math.cos(theta))
    y=float((v*t*math.sin(theta))-(0.5*9.81*t*t))
    if y+1>h1 and y+1<h2:
        print("Safe")
    else:
        print("Not Safe")


