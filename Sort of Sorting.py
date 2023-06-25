import functools


def modify_sort(name1, name2):
    if name1[0] < name2[0]:
        return -1
    elif name2[0] < name1[0]:
        return 1
    elif name1[1] < name2[1]:
        return -1
    elif name2[1] < name1[1]:
        return 1
    else:
        return 0


i = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if i > 0:
            print()
        names = []
        for _ in range(n):
            last_name = input()
            names.append(last_name)
        names.sort(key=functools.cmp_to_key(modify_sort))
        for name in names:
            print(name)
        i += 1
