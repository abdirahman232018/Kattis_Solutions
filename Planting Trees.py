n = int(input())
days = [int(d) + 1 for d in input().split()]
days.sort(reverse=True)
earliest_day = 0
for i in range(n):

    if days[i] + i > earliest_day:
        earliest_day = days[i] + i

print(earliest_day + 1)