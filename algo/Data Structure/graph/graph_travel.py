from collections import deque


def DFS(graph, start):
    stack = [start]
    visited = set()
    visited.add(start)
    while stack:
        node = stack.pop()
        nodes = graph[node]
        for w in nodes:
            if w not in visited:
                stack.append(w)
                visited.add(w)
        print(node, end=" ")
    print()


def BFS(graph, start):
    visited = set()
    queue = deque()
    visited.add(start)
    queue.append(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
        print(node, end=" ")
    print()


# 初始化圖
edges = {1: [2, 5], 2: [1,3, 4], 3: [2, 4, 5], 4: [2, 3, 5], 5: [1, 3, 4]}
print("DFS traversal: ")
DFS(edges, 1)
print("BFS traversal: ")
BFS(edges, 1)
