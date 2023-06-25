c = int(input())
def getAv(arr,n):
    return sum(arr)/n

for i in range(c):
    dataset = input().split()
    dataset=[float(d) for d in dataset]
    n=int(dataset[0])
    av = getAv(dataset[1::],n)
    ab_av = 0
    for j in range(n):
        if int(list(dataset)[j+1]) > av:
            ab_av += 1
    per =(ab_av /n ) * 100
    per=("%.3f" % per)
    print(str(per)+"%")



