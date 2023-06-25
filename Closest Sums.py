import sys
from sys import stdin, stdout


def closestSum(arr, querry):
    a = sorted(arr)
    l, r = 0, len(arr) - 1
    res = -1
    min_diff = sum(arr)
    while l < r:

        if a[l] + a[r] <= querry:
            res = max(res, a[l] + a[r])
            l += 1
        else:
            if abs((a[l] + a[r]) - querry) < min_diff:  # min sum
                min_diff = a[l] + a[r]
            r -= 1
    if res == -1:
        return min_diff

    return min(res, min_diff)
case_count = 1
# line = stdin.readline()
# while line!="":
#
#     try:
#         line = int(line)
#     except ValueError:
#         break
#     distinct_ints = []
#     for i in range(int(line)):
#         dist_int = int(stdin.readline())
#
#         distinct_ints.append(dist_int)
#     m = int(stdin.readline())
#
#     stdout.write("Case " + str(case_count) + ":")
#     stdout.write('\n')
#     for j in range(m):
#         query = int(stdin.readline())
#         closest_sum = closestSum(distinct_ints, query)
#         stdout.write("Closest sum to " + str(query) + " is " + str(closest_sum) + ".")
#         stdout.write('\n')
#     case_count += 1
#
#     line = stdin.readline()

while True:

    try:
        line = int(input())
    except EOFError:
        break
    distinct_ints = []
    for i in range(int(line)):
        dist_int = int(stdin.readline())

        distinct_ints.append(dist_int)
    m = int(stdin.readline())

    stdout.write("Case " + str(case_count) + ":")
    stdout.write('\n')
    for j in range(m):
        query = int(stdin.readline())
        closest_sum = closestSum(distinct_ints, query)
        stdout.write("Closest sum to " + str(query) + " is " + str(closest_sum) + ".")
        stdout.write('\n')
    case_count += 1
