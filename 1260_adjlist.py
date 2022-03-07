import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n,m,v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
for i in range(n+1):
    arr[i].sort()

def dfs(start, visited = []):
    visited.append(start)
    print(start, end = " ")
    for i in arr[start]:
        if i not in visited:
            dfs(i, visited)

def dfs_iter(start):
    visited = []
    stack = deque([start])
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end = " ")
            visited.append(node)
            stack.extend(reversed(arr[node]))


def bfs(start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(arr[node])

dfs(v)
print()
dfs_iter(v)
print()
bfs(v)
