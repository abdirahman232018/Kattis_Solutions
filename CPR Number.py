num=input()

mul_vals=[4,3,2,7,6,5,4,3,2,1]
sum1=0
for i in range(len(num)):
    if i<6:
        cur_num=int(num[i])
        sum1+=(cur_num*mul_vals[i])
    if i>6:
        cur_num = int(num[i])
        sum1 += (cur_num * mul_vals[i-1])


if sum1%11==0:
    print(1)
else:
    print(0)