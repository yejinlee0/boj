from collections import deque
n = int(input())
k = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r-1][c-1] = 1
L = int(input())
change = []
for _ in range(L):
    tmp1, tmp2 = input().split()
    change.append([int(tmp1), tmp2])

hr, hc = 0, 0
body = deque()
body.append([0,0])

# 오 아래 왼 위 - 시계 방향
move_dir = [[0,1],[1,0],[0,-1],[-1,0]]
time = 0
dir = 0
idx = 0

def in_range(r, c):
    if 0<=r<n and 0<=c<n:
        return 1
    return 0

while True:
    time += 1

    nr, nc = hr + move_dir[dir][0], hc + move_dir[dir][1]

    if (in_range(nr, nc) == 0) or ([nr,nc] in body):
        break

    body.append([nr, nc])
    if grid[nr][nc] == 1:
        grid[nr][nc] = 0
    else:
        body.popleft()

    if idx < L and time == change[idx][0]:
        if change[idx][1] == 'L':
            dir = (dir + 3) % 4
        else:
            dir = (dir + 1) % 4
        idx += 1

    hr, hc = nr, nc

print(time)
