line = input().split()
h = int(line[0])
r = (2 ** (h + 1)) - 1

if line[0] == line[-1]:
    print(r)
else:
    num = r
    path = line[-1]
    path=path[::-1]
    path_len = len(path)
    level_size = 1

    for d in path:

        if d == "L":

            num -= level_size
            level_size *= 2
        else:
            level_size *= 2
            num -= level_size

    print(num)
