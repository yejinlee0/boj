from collections import deque
n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

move_dir = [[-1,0],[0,-1],[1,0],[0,1]]
result = 0

def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return 1
    return 0

def gravity():
    global grid
    for j in range(n):
        for i in range(n-2,-1,-1):
            if grid[i][j] < 0:
                continue
            if grid[i+1][j] >= -1:
                continue
            for k in range(i+1,n,1):
                if grid[k][j] != -2:
                    k -= 1
                    break
            grid[k][j] = grid[i][j]
            grid[i][j] = -2

    return

def rotate():
    tmp = [[-2 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = grid[j][n-1-i]

    return tmp

def bfs(r, c, num, check):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([r,c])
    visited[r][c] = True
    check[r][c] = True
    cnt = 1
    rainbow = 0
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr + move_dir[i][0], cc + move_dir[i][1]
            if in_range(nr, nc) == 1 and visited[nr][nc] == False:
                if grid[nr][nc] == 0 or grid[nr][nc] == num:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
                    cnt += 1
                    if grid[nr][nc] == 0:
                        rainbow += 1
                    else:
                        check[nr][nc] = True

    return cnt, rainbow, check

def remove_block(r, c):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([r,c])
    visited[r][c] = True
    cnt = 1
    num = grid[r][c]
    grid[r][c] = -2
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr + move_dir[i][0], cc + move_dir[i][1]
            if in_range(nr, nc) == 1 and visited[nr][nc] == False:
                if grid[nr][nc] == 0 or grid[nr][nc] == num:
                    visited[nr][nc] = True
                    queue.append([nr, nc])
                    cnt += 1
                    grid[nr][nc] = -2
    return cnt**2

while True:
    check = [[False for _ in range(n)] for _ in range(n)]
    mcnt, mrbw = -1, -1
    mrow, mcol = -1, -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0 and check[i][j] == False:
                tcnt, trbw, check = bfs(i, j, grid[i][j], check)
                if tcnt < 2:
                    continue
                if tcnt < mcnt:
                    continue
                if tcnt == mcnt:
                    if trbw < mrbw:
                        continue
                    if trbw == mrbw:
                        if i < mrow:
                            continue
                        if i == mrow:
                            if j < mcol:
                                continue
                mcnt, mrbw = tcnt, trbw
                mrow, mcol = i, j

    if mcnt == -1:
        break

    result += remove_block(mrow, mcol)

    gravity()

    grid = rotate()

    gravity()

print(result)

# if 문 대신 list에 추가해서 sort 하는 방법도 
