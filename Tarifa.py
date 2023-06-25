x=int(input())
n=int(input())
total_unused=0
for i in range(n):
    used=int(input())
    rem=x-used
    total_unused+=rem


print(x+total_unused)