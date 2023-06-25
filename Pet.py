team_points=0
winner=1

for i in range(1,6):
    contestants=list(map(int,input().split()))
    cur_sum=sum(contestants)
    if cur_sum>team_points:
        winner=i
        team_points=cur_sum


print(winner,team_points)