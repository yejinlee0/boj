from collections import deque

N = int(input())
M = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1][c2] = arr[c2][c1] = 1

vis = []
def dfs(start, visited = []):
    visited.append(start)
    for w in range(1,N+1):
        if arr[start][w] == 1 and w not in visited:
            dfs(w, visited)
    return len(visited) - 1

print(dfs(1,vis))
