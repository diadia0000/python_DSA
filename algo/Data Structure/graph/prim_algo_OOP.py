import heapq
from heapq import *


class Graph:
    def __init__(self, ver):
        self.V = ver
        self.graph = [[] for i in range(ver)]

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prime(self):
        min_heap = [(0, 0)]
        visited = [False] * (self.V)
        cost = 0
        while min_heap:
            weight, u = heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            cost += weight
            for v, w in self.graph[u]:
                if not visited[v]:
                    heappush(min_heap, (w, v))
        if all(visited):
            return cost
        return -1


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.addEdge(u, v, w)
print(graph.prime())
