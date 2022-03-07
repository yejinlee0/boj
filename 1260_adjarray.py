from collections import deque

def dfs(start_v, visited=[]):
    visited.append(start_v)
    print(start_v, end = " ")
    for w in range(1, N+1):
        if graph[start_v][w] == 1 and (w not in visited):
            dfs(w, visited)

def bfs(start_v):
    queue = deque()
    queue.append(start_v)
    visited = [start_v]
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for w in range(1,N+1):
            if graph[node][w] == 1 and (w not in visited):
                queue.append(w)
                visited.append(w)


N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

dfs(V)
print()
bfs(V)
