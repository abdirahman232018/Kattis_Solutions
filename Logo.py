import math
def getDistance(x,y):
    return math.dist([0,0],[x,y])
T=int(input())

for _ in range(T):
    number_commands=int(input())
    x,y=0,0
    dir=[0,1]


