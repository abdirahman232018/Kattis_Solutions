def getArea(x_a, y_a,x_b, y_b,x_c, y_c):
    return (abs(x_a*(y_b-y_c)+x_b*(y_c-y_a)+x_c*(y_a-y_b)))/2

x_a, y_a = list(map(int, input().split()))
x_b, y_b = list(map(int, input().split()))
x_c, y_c = list(map(int, input().split()))
A=getArea(x_a, y_a,x_b, y_b,x_c, y_c)
N=int(input())
apple_trees=0
for _ in range(N):
    x, y = list(map(int, input().split()))
    A1=getArea(x, y,x_b, y_b,x_c, y_c)
    A2=getArea(x_a, y_a,x, y,x_c, y_c)
    A3=getArea(x_a, y_a,x_b, y_b,x, y)
    if A==(A1+A2+A3):
        apple_trees+=1

print(A)
print(apple_trees)