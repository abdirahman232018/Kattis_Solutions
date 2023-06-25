est=int(input())
def count_digit(d):
    c=0
    for i in d:
        c+=1
    return c


for i in range(est):
    dig=input()
    print(count_digit(dig))