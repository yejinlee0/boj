import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
year = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr = cr + dy[i]
            nc = cc + dx[i]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and ice[nr][nc] != 0:
                visited[nr][nc] = 1
                queue.append([nr,nc])
            elif 0<=nr<N and 0<=nc<M and ice[nr][nc] == 0:
                surrice[cr][cc] += 1

while True:
    visited = [[0]*M for _ in range(N)]
    surrice = [[0]*M for _ in range(N)]
    pc = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if ice[i][j] != 0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i,j)
                pc += 1

    if pc == 0:
        year = 0
        break

    if pc > 1:
        break

    year += 1
    for i in range(1,N-1):
        for j in range(1,M-1):
            ice[i][j] -= surrice[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0

print(year)
