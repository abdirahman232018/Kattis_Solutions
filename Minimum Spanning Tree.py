
def addEdge(g,u,v):
   g[u].add(v)
   g[v].add(u)
def buildGraph():
   pass

while True:

   line=list(map(int,input().split()))
   if line[0]==0 and line[-1]==0 and len(line)==2:
      break
   else:
      n=line[0]
      m=line[1]
      graph={}
      for i in range(n):
          graph[i]=set()

      for _ in range(m):
         u,v,w = list(map(int, input().split()))
         graph[u].add(v)
         graph[v].add(u)












