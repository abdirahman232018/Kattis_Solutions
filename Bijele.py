pieces = list(map(int, input().split()))
val_set=[1,1,2,2,2,8]
for i in range(len(pieces)):
    val_set[i]=str(val_set[i]-pieces[i])





print(" ".join(val_set))