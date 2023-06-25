abc_int=list(map(int, input().split()))
a=min(abc_int)
abc_int.remove(a)
c=max(abc_int)
abc_int.remove(c)
b=abc_int[0]

abc_str=input()

if abc_str[0]=="A":
    if abc_str[1]=="B":
        print(a,b,c)
    if abc_str[1]=="C":
        print(a,c,b)

elif abc_str[0]=="B":
    if abc_str[1]=="C":
        print(b,c,a)
    if abc_str[1]=="A":
        print(b,a,c)

else:
    if abc_str[1]=="B":
        print(c,b,a)
    if abc_str[1]=="A":
        print(c,a,b)


