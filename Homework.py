problem_list=input().split(";")
sum1=0

for p in problem_list:

    if "-" not in p:
        sum1+=1
    else:
        p2=list(map(int,p.split("-")))
        sum1+=(p2[1]-p2[0])+1



print(sum1)