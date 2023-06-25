s=input()
hiss=False
for i in range(1,len(s)):
    if s[i-1]==s[i] and s[i]=="s":
        hiss=True
        break

if hiss:
    print("hiss")
else:
    print("no hiss")