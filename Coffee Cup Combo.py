lecs=int(input())
lec_seq=input()
awake=0
for l in lec_seq:
    if l=="1":
        awake+=1
if awake==0:
    print(0)
else:
    print(2**awake)