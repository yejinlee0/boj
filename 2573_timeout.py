import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
year = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(r,c):
    for i in range(4):
        nr = r + dy[i]
        nc = c + dx[i]
        if 0 <= nc < M and 0 <= nr < N and ice[nr][nc] != 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr,nc)

while True:
    visited = [[0]*M for _ in range(N)]
    pc = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if ice[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i,j)
                pc += 1

    if pc == 0:
        year = 0
        break

    if pc > 1:
        break

    year += 1
    for i in range(1,N-1):
        for j in range(1,M-1):
            surr = 0
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0<=x<M and 0<=y<N and ice[y][x] == 0:
                    surr += 1
            ice[i][j] -= surr
            if ice[i][j] < 0:
                ice[i][j] = 0

print(year)
