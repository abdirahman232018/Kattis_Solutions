import math


N = int(input())

for _ in range(N):
    m = int(input())
    cur_angle = 90
    x, y = 0.0, 0.0

    for j in range(m):
        a, d = list(map(float, input().split()))

        cur_angle += a
        x += (math.cos(math.radians(cur_angle))) * d
        y += (math.sin(math.radians(cur_angle))) * d

    print("%.6f" % x, "%.6f" % y)
