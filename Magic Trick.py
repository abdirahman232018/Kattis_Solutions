s=input()

set_s=set()
pos=1
for c in s:
    if c in set_s:
        pos=0
        break
    else:
        set_s.add(c)
print(pos)
