from collections import deque
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
sr, sc = 0, 0
baby_size = 2
time = 0
M = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = tmp[j]
        if tmp[j] == 9:
            sr, sc = i, j
        elif tmp[j] != 0:
            M += 1

eat = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def in_range(r, c):
    if 0<=r<N and 0<=c<N:
        return 1
    return 0

def move(r, c):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([r, c, 0])
    visited[r][c] = 1
    possible = []

    while queue:
        cr, cc, cstep = queue.popleft()
        for i in range(4):
            nr, nc, nstep = cr + dr[i], cc + dc[i], cstep + 1
            if in_range(nr,nc) and visited[nr][nc] == 0 and arr[nr][nc] <= baby_size:
                visited[nr][nc] = 1
                if 0 < arr[nr][nc] < baby_size:
                    possible.append([nstep, nr, nc])
                else:
                    queue.append([nr,nc,nstep])
                    
    if len(possible) == 0:
        return 0, -1, -1
    possible.sort(key = lambda x:(x[0],x[1],x[2]))
    return possible[0][0], possible[0][1], possible[0][2]

eat = 0
arr[sr][sc] = 0
while M:
    step = 0
    step, sr, sc = move(sr, sc)
    if sr == -1 and sc == -1:
        break
    eat += 1
    arr[sr][sc] = 0

    if eat == baby_size:
        baby_size += 1
        eat = 0
    time += step

print(time)

# 최단거리는 절댓값 거리가 아님. 돌아가는 방법이 최단거리일수도 있음.
