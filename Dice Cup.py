data = input().split()
die1 = int(data[0])
die2 = int(data[1])

lower = min(die1, die2)
higher = max(die1, die2)

for num in range(lower + 1, higher + 2):
    print(num)