line=input()

whitespace=0
lower=0
upper=0
symbols=0
for c in line:
    if c=="_":
        whitespace+=1
    elif ord(c)>=65 and ord(c)<=90:
        upper+=1
    elif ord(c)>=97 and ord(c)<=122:
        lower+=1
    else:
        symbols+=1


print("%.6f"%(whitespace/len(line)))
print("%.6f"%(lower/len(line)))
print("%.6f"%(upper/len(line)))
print("%.6f"%(symbols/len(line)))