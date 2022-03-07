N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
graph = [[0]*N for _ in range(N)]

dc = [0,1,0,-1]
dr = [1,0,-1,0]

cnt = 1
def dfs(start, visited=[]):
    visited.append(start)
    r = start[0]
    c = start[1]
    graph[r][c] = cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nc >= 0 and nr < N and nc < N:
            if arr[nr][nc] == 1 and [nr,nc] not in visited:
                dfs([nr,nc], visited)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and graph[i][j] == 0:
            dfs([i,j])
            cnt += 1

num = [0] * (cnt-1)
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            num[graph[i][j] - 1] += 1

num.sort()
print(cnt-1)
for i in range(cnt-1):
    print(num[i])
