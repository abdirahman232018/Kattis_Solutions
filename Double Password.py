

p1 = input()
p2 = input()

combinations = 1
for d1, d2 in zip(p1, p2):
    if d1 != d2:
        combinations *= 2

print(combinations)