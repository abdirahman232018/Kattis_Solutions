poker_hand={}


hand=input().split()

for card in hand:
    rank=card[0]
    if rank not in poker_hand.keys():
        poker_hand[rank]=1
    else:
        prev_val=poker_hand[rank]+1
        poker_hand[rank]=prev_val

print(max(poker_hand.values()))


