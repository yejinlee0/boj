# 최소를 찾아야 할 때는 bfs 쓰는 게 더 편함
from collections import deque

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1][v2] = arr[v2][v1] = 1

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for i in range(1, N+1):
            if arr[node][i] == 1 and visited[i] == 0:
                visited[i] += (visited[node] + 1)
                queue.append(i)

bfs(p1)
if visited[p2] == 0:
    print(-1)
else:
    print(visited[p2]-1)

