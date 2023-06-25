def isPrefix(string, length, i, k):

    if i + k > length:
        return False

    for j in range(0, k):

        if string[i] != string[j]:
            return False
        i += 1

    return True


# Function that returns true if
# str is K-periodic
def isKPeriodic(string, length, k):
    # Check whether all the sub-strings
    # str[0, k-1], str[k, 2k-1] ... are equal
    # to the k length prefix of the string
    for i in range(k, length, k):
        if isPrefix(string, length, i, k) == False:
            return False
    return True

s=input()
n=len(s)
flag=True
for k in range(1,n):
    if n%k==1:
        if isKPeriodic(s,n,k):
            flag=False
            print(k)
            break


if flag:
    print(n)




