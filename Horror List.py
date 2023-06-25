import math
def getPar(par,v):
    if par[v]==v:
        return v
    p=par[v]
    while p!=par[p]:
        p=par[p]
    return p



n_movies, horror_list, l_similarities = list(map(int, input().split()))

horror_list_ids = list(map(int, input().split()))

movies_hi=[-1 for i in range(n_movies)]
movies_par=[-1 for j in range(n_movies)]
for h in horror_list_ids:
    movies_hi[h]=0
    movies_par[h]=0

for _ in range(l_similarities):
    a,b=list(map(int, input().split()))

    if movies_hi[a]==0 and movies_hi[0]:
        continue
    elif movies_hi[a] == 0 and movies_hi[b]==-1:
        movies_par[b] = 0
        movies_hi[b] = 1

    elif movies_hi[b] == 0 and movies_hi[a]==-1:
        movies_par[a] = 0
        movies_hi[a] = 1
    elif movies_hi[a] == -1 and movies_hi[b]==-1:
        movies_par[b] = a
    elif movies_hi[a] == 1 and movies_hi[b]==-1:
        movies_hi[b] = movies_hi[a]+1
        movies_par[b] = a
    else:

        p1=getPar(movies_par,a)
        movies_par[a] = p1
        movies_par[b] = p1



















print(movies_hi)
print(movies_par)
















#movies_par=[i for i in range(n_movies)]
# for h in horror_list_ids:
#     movies_hi[h]=0
#
#
# for _ in range(l_similarities):
#     a,b=list(map(int, input().split()))
#     if movies_hi[a]==0 and movies_hi[b]!=0:
#         movies_hi[b]=1
#     elif movies_hi[b]==0 and movies_hi[a]!=0:
#         movies_hi[a]=1
#     elif movies_hi[a]==1 and movies_hi[b]==-1:
#         movies_hi[b]=movies_hi[a]+1
#     elif movies_hi[b]==1 and movies_hi[a]==-1:
#         movies_hi[a]=movies_hi[b]+1
#     elif movies_hi[a]>1 and movies_hi[b]==-1:
#         movies_hi[b]=movies_hi[a]+1
#     elif movies_hi[b]>1 and movies_hi[a]==-1:
#         movies_hi[a]=movies_hi[b]+1
#     else:
#         if movies_hi[a]!=0 and movies_hi[b]!=0:
#             if movies_hi[a]!=1 and movies_hi[b]!=1:
#                 movies_hi[a]=math.inf
#                 movies_hi[b]=math.inf
#
#
#
#
#
#
# min_hi=0
#
# for m in range(n_movies):
#
#     if movies_hi[m]!=-1:
#         if movies_hi[m]>movies_hi[min_hi]:
#             min_hi=m
#     else:
#         movies_hi[m]=0
# print(min_hi)

