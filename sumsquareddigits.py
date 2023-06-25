def get_base_b(b, n):
    b1 = ""
    rem = n
    while rem > 0:
        b1 += str(rem % b)
        rem = rem // b
    return b1
def convert_digits(digs_str):
    sum1 = 0

    for d in digs_str:
        d = int(d)
        sum1 += d * d
    return sum1

P=int(input())


for i in range(P):
    j,b,n=list(map(int,input().split()))
    k=get_base_b(b,n)
    print(j,convert_digits(k))


