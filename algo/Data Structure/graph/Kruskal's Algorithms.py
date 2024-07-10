class graph:
    def __init__(self,ver):
        self.V = ver
        self.graph = []
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self,parent,i):
        if parent[i] != i:
            parent[i] = self.find(parent,parent[i])
        return parent[i]
    def union(self,parent,rank,x,y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] >rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x]+=1
    def Kruskal(self):
        result = []
        i = 0 ; e = 0
        self.graph = sorted(self.graph,key=lambda x:x[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1: # 邊的個數
            if i >= len(self.graph):
                return -1
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        min_cost = 0
        for u,v,w in result:
            min_cost+=w
        return min_cost
while True:
    try:
        n,m = map(int,input().split())
        g = graph(n)
        for i in range(m):
            u,v,w = map(int,input().split())
            g.addEdge(u,v,w)
        print(g.Kruskal())
    except EOFError:
        break