nk=input().split()
n,k=int(nk[0]),int(nk[1])

max_add=(n-k)*3
min_add=(n-k)*-3

prev_total_rate=0
for i in range(k):
    rate=int(input())
    prev_total_rate+=rate


print((prev_total_rate+min_add)/n,(prev_total_rate+max_add)/n)
