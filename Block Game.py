
small, big = sorted(list(map(int, input().split())))

res = ["win", "lose"]
turn,i = 1,0
while True:


    if big % small == 0:
        print(res[i])
        break
    elif small == 1 :
        print(res[i])
        break
    else:

        num = big // small

        big -= (num * small)

        if num > 1:
            if turn:
                print("win")
                break
            else:
                print('lose')
                break
        big,small=small,big

    i = 1 - i

    turn = 1 - turn