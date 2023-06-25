phrase=input().split(" ")
repeat=False
phrase_set=set()
for p in phrase:
    if p in phrase_set:
        repeat=True
        break
    else:
        phrase_set.add(p)

if not repeat:
    print("yes")
else:
    print("no")