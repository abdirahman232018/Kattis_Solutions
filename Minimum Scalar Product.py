test_cases=int(input())


for i in range(test_cases):
    n=int(input())
    line1=[int(v1) for v1 in input().split()]
    line1.sort(reverse=True)
    line2 = [int(v2) for v2 in input().split()]
    line2.sort()
    minimum_scalar_product=0
    for j in range(n):
        minimum_scalar_product+=line1[j]*line2[j]
    print("Case #"+str(i+1)+": "+str(minimum_scalar_product))
