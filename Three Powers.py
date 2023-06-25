
while True:
    n = int(input())
    if n == 0:
        break
    sub = []
    n -= 1
    cur = 1
    while n!=0:
        if n % 2 != 0:
            sub.append(str(cur))
        cur *= 3
        n = n >> 1

    if not sub:
        print("{ }")
    else:
        print("{{ {} }}".format(", ".join(sub)))