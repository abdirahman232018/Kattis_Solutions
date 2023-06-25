fate=["magic", "left", "right", "cycle"]

nsm=input().split()
n,s,m=int(nsm[0]),int(nsm[1]),int(nsm[2])
board_squares=input().split()

already_visited=set()
cur=s
already_visited.add(s)
if s==m:
    print(fate[0])
    print(0)
else:
    h=0
    for i in range(len(board_squares)):

        sq=int(board_squares[i])



        if sq==m:
            print(fate[0])
            print(h)
            break
        elif sq<-200:
            print(fate[1])
            print(h)
            break
        elif sq>200:
            print(fate[2])
            print(h)
            break
        if sq in already_visited:
            print(fate[3])
            print(i+1)
            break

        else:
            already_visited.add(sq)
            h += 1


