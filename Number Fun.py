lines = int(input())
for i in range(lines):
    abc = input().split()
    abc = [int(j) for j in abc]

    if abc[0] + abc[1] == abc[2]:
        print("Possible")
    elif abs(abc[0] - abc[1]) == abc[2]:
        print("Possible")
    elif abc[0] == abc[1] * abc[2] or abc[1] == abc[0] * abc[2]:
        print("Possible")
    elif abc[0] * abc[1] == abc[2]:
        print("Possible")
    else:
        print("Impossible")