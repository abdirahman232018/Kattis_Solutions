import math
def getOtherpoint(mx,my,x1,y1):
    x= int((2 * mx) - x1)
    y = int((2 * my) - y1)
    print(x,y)

def getDistance(p, q):
    return math.dist(p, q)

def getOrderABC(A, B, C):

    if getDistance(A,B)>getDistance(A,C):
        midx, midy = (A[0] +B[0]) / 2, (A[1] + B[1]) / 2
        getOtherpoint(midx,midy,C[0],C[1])
    elif getDistance(A,B)<getDistance(A,C):
        midx, midy = (A[0] + C[0]) / 2, (A[1] + C[1]) / 2
        getOtherpoint(midx, midy, B[0], B[1])
    else:
        midx, midy = (B[0] + C[0]) / 2, (B[1] + C[1]) / 2
        getOtherpoint(midx, midy, A[0], A[1])

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
getOrderABC(A,B,C)
