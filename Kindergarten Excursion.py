

str1=input()


digits = [0,0,0]
res = 0
r = [range(i + 1, 3) for i in range(3)]
for d in map(int, str1):
    for j in r[d]:
        res += digits[j]
    digits[d] += 1
print(res)