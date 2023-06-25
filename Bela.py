line = input().split()
N=int(line[0])
suitB=line[1]

nums={"A":[11], "K":[4], "Q":[3], "J":[20,2], "T":[10], "9":[14,0], "8":[0], "7":[0]}
points=0
for _ in range(N):
    hand=0
    i=0
    while i<4:
        card=input()
        card_num,card_suit=card[0],card[1]


        #if dominant
        if card_suit==suitB:
            val1=nums[card_num]
            hand+=val1[0]
        # else
        else:
            val1 = nums[card_num]
            hand += val1[-1]
        i+=1
    points+=hand
print(points)