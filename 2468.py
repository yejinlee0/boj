import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

maxh = 0
N = int(input())
arr = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    h = max(tmp)
    if h > maxh:
        maxh = h
    arr.append(tmp)

safe = 0

dc = [-1,1,0,0]
dr = [0,0,-1,1]

def dfs(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc] > ht and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr,nc)

for ht in range(0,maxh+1):
    visited = [[0] * N for _ in range(N)]
    safetmp = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > ht and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i,j)
                safetmp += 1
    if safetmp > safe:
        safe = safetmp

print(safe)

# 비가 오지 않는 경우도 고려. 안전 영역 같은 문제의 경우 dfs가 편함.
