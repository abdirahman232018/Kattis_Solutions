T=int(input())
for _ in range(T):
    n=int(input())
    flag=True
    phone_list=set()
    smallest=input()
    m=len(smallest)
    phone_list.add(smallest)
    for j in range(n-1):
        p=input()
        if len(p)<=m:
            smallest=p
            m=len(p)
        phone_list.add(p)
    phone_list.remove(smallest)
    for p1 in phone_list:
        if p1[0:m]==smallest:
            print(smallest)
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")



