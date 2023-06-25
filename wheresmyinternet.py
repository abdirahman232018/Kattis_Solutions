#


#
# def union(h1, h2,root):
#     rootX = find(h1,root)
#     rootY = find(h2,root)
#     if rootX != rootY:
#         for i in range(len(root)):
#             if root[i] == rootY:
#                 root[i] = rootX
#
# def connected( h1, h2,root):
#     return find(h1,root) == find(h2,root)

n_m = input().split()
houses = int(n_m[0])
lines = int(n_m[1])
root = [i for i in range(houses+1)]
root[1]=0



def find(h):
    global root
    if root[h] == h:
        return h
    else:
        nodes = set()
        nodes.add(h)
        par = root[h]
        nodes.add(par)
        while par != root[par]:
            par = root[par]
            nodes.add(par)
        for p in nodes:
            root[p] = par
        return par
for i in range(lines):

    edge = input().split()
    h1, h2 = int(edge[0]), int(edge[1])
    smaller=min(h1,h2)
    if h1==smaller:
        root[h2]=root[h1]
    elif h2==smaller:
        root[h1] = root[h2]
    else:
        root[h1]=root[h2]

all_connected=True

for j in range(1,houses+1):
    if find(j)!=0:
        print(j)
        all_connected=False

if all_connected:
    print("Connected")