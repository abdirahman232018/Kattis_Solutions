import math
line=input().split()
matches=int(line[0])
w=int(line[1])
h=int(line[2])
dig=int(math.sqrt((w*w)+(h*h)))
for i in range(matches):
    w2=int(input())

    if w2<=w or w2<=h or w2<=dig:
        print("DA")
    else:
        print("NE")



