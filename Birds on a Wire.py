ldn=input().split()
l,d,n=int(ldn[0]),int(ldn[1]),int(ldn[2])
pos=[0]*(l-5)

num_birds=0

for i in range(n):
    bird_pos=int(input())
    pos[bird_pos]=1

if n==0:
    num_birds=((l-12)//d)+1

else:
    for k in range(6,len(pos)):
        if pos[k]==1:
            temp=k
            while k-d>=6:
                if pos[k-d]==0:
                    num_birds+=1
                k-=d
            while temp<=l-6:
                if pos[temp]==0:
                    num_birds+=1
                temp+=d
            break


print(num_birds)

