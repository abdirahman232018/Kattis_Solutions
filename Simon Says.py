n=int(input())


for i in range(n):
    line=input().split(" ")

    if line[0]=="Simon" and line[1]=="says" and len(line)>=3:

        print(" ".join(line[2::]))



