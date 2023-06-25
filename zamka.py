def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

l=int(input())
d=int(input())
x=int(input())
n=0
m=0
for i in range(l,d+1):
    if getSum(i)==x:
        n=i
        break
for j in range(d,l-1,-1):
    if getSum(j)==x:
        m=j
        break
print(n)
print(m)

