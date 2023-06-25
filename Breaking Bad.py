import sys
N=int(input())
jess=set()
walt=set()
required_items={}
for _ in range(N):
    it=input()
    required_items[it]=""
M=int(input())

for p in range(M):
    p1,p2=input().split()
    required_items[p1]=p2
    required_items[p2]=p1

j=0
imposs=False
for item1 in required_items:
    if j==N:
        break
    else:
        if required_items[item1]=="":
            walt.add(item1)
            j+=1
        else:
            sus_item=required_items[item1]
            #safe for walt
            if sus_item not in walt:
                if sus_item in jess:
                    pass
                else:
                    pass









print(required_items)

print(walt)
print(jess)





