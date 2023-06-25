import sys

line = input()
while True:
    try:
        n = int(line)
    except:
        sys.exit(0)
    slots = [0] * n
    miles = 0
    for i in range(n):
        line = input().split()
        speed, t = int(line[0]), int(line[1])
        if i == 0:
            miles += speed * t
            slots[i] = t
        else:
            t2 = t - slots[i - 1]
            miles += speed * t2
            slots[i] = t
    print(str(miles)+" miles")

    line = input()
    if line == "-1":
        break
