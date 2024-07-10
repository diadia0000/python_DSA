import heapq
from sys import stdin
def prim_mst(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    min_heap = [(0, 0)]  # (weight, vertex)
    visited = [False] * n
    mst_cost = 0
    mst_edges = []
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
        if weight != 0:
            mst_edges.append((u, weight))
    if all(visited):
        return mst_cost
    else:
        return -1
# Usage
while True:
    try:
        n, m = list(map(int, stdin.readline().strip("\n").split()))
        edges = []
        for _ in range(m):
            u, v, w = map(int,stdin.readline().strip("\n").split())
            edges.append((u, v, w))

        result = prim_mst(n, edges)
        if result == -1:
            print(-1)
        else:
            mst_cost = result
            print(mst_cost)
    except:
        break