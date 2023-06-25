
lines=10
N=42
dist_vals=set()
for _ in range(lines):
    num=int(input())
    dist_vals.add(num%N)
print(len(dist_vals))


