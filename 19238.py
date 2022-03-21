from collections import deque

n, m, oil = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
sr, sc = sr - 1, sc - 1
sonnim = []
step = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    sonnim.append([r1 - 1, c1 - 1, r2 - 1, c2 - 1])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return 1
    return 0

def count_possible(r, c):
    global step
    visited = [[False for _ in range(n)] for _ in range(n)]
    step = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append([r, c])
    step[r][c] = 0
    visited[r][c] = True ##
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if in_range(nr, nc) and grid[nr][nc] == 0 and visited[nr][nc] == False:
                visited[nr][nc] = True
                queue.append([nr, nc])
                step[nr][nc] = step[cr][cc] + 1

    return

while sonnim:
    min_val, idx = n*n+n, -1
    min_r, min_c = 0, 0
    count_possible(sr, sc)

    for i in range(m):
        start_r, start_c, dest_r, dest_c = sonnim[i]
        if step[start_r][start_c] == -1 or step[start_r][start_c] > oil:
            continue
        elif step[start_r][start_c] < min_val:
            min_val = step[start_r][start_c]
            idx = i
            min_r, min_c = start_r, start_c
        elif step[start_r][start_c] == min_val:
            if (start_r < min_r) or (start_r == min_r and start_c < min_c):
                min_val = step[start_r][start_c]
                idx = i
                min_r, min_c = start_r, start_c

    if min_val > oil or min_val == n*n+n:
        oil = -1
        break

    oil -= min_val

    start_r, start_c, dest_r, dest_c = sonnim.pop(idx)
    sr, sc = start_r, start_c

    count_possible(sr, sc)

    if step[dest_r][dest_c] == -1 or step[dest_r][dest_c] > oil:
        oil = -1
        break
    else:
        oil += step[dest_r][dest_c]
        m -= 1
        sr, sc = dest_r, dest_c

print(oil)
