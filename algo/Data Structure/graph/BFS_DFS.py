from collections import deque


def BFS(graph, start):
    ans = []
    queue = deque()
    visited = set()
    queue.appendleft(start)
    visited.add(start)
    while len(queue) > 0:
        vertex = queue.popleft()
        ans.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return ans


def DFS(graph, start):
    ans = []
    queue = deque()
    visited = set()
    queue.appendleft(start)
    visited.add(start)
    while len(queue) > 0:
        vertex = queue.popleft()
        ans.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.appendleft(neighbor)
                visited.add(neighbor)
    return ans


grahp = {"A": ["B", "C"],
         "B": ["A", "C"],
         "C": ["A", "D", "B"],
         "D": ["E", "C"],
         "E": ["D"]
         }
print(BFS(grahp, "A"))
print(DFS(grahp, "A"))