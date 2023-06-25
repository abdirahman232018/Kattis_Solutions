n=int(input())


for i in range(n):
    r_e_c=input().split()
    r,e,c=int(r_e_c[0]),int(r_e_c[1]),int(r_e_c[2])
    if r+c<e:
        print("advertise")
    elif r+c==e:
        print("does not matter")
    else:
        print("do not advertise")
