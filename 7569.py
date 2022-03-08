from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
M,N,H = map(int, input().split())
#box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# arr[차원][row][col]
box = []
queue = deque()
for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        for k in range(M):
            if tmp[j][k] == 1 :
                queue.append([i,j,k])
    box.append(tmp)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while queue:
    z,y,x = queue.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<M and 0<=ny<N and 0<=nz<H:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append([nz,ny,nx])

day = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            if k > day:
                day = k

print(day-1)

# bfs는 걸리는 시간을 알아내는 데에 사용될 수 있다.
