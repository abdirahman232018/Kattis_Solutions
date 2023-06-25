x1,y1,x2,y2=list(map(float,input().split()))

x,y=0,0

if x1>=x2:
    x+= (x1 - x2)
if x1<x2:
    x += (x2 - x1)
if y1>=y2:
    y += (y1 - y2)
if y1<y2:
    y += (y2 - y1)


print("%.2f"%(x*y))