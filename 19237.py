n,m,k = map(int, input().split())
# 1부터 m번
grid = [list(map(int, input().split())) for _ in range(n)]
move_dir = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]
# 0부터 m-1 번 상어
shark_dir = list(map(int, input().split()))
priority = [[] for _ in range(m)]

for i in range(m):
    for _ in range(4):
        tmp = list(map(int, input().split()))
        priority[i].append(tmp)

# 1번부터 m번
frag = [[[0,0] for _ in range(n)] for _ in range(n)]

time = 0

# 냄새 뿌리기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            continue
        frag[i][j] = [grid[i][j], k]

def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return 1
    return 0

while True:
    time += 1
    #상어 이동하기
    tmp = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            crt_dir = shark_dir[grid[i][j]-1]
            cr, cc = -1, -1
            cdir = -1
            for p in range(4):
                next_dir = priority[grid[i][j]-1][crt_dir-1][p]
                nr,nc = i+move_dir[next_dir][0], j+move_dir[next_dir][1]
                if in_range(nr,nc) == 0:
                    continue
                if frag[nr][nc][0] == 0:
                    cr, cc = nr, nc
                    cdir = next_dir
                    break
                if frag[nr][nc][0] == grid[i][j] and cr == -1 and cc == -1:
                    cr, cc = nr, nc
                    cdir = next_dir
            tmp[cr][cc].append(grid[i][j])
            shark_dir[grid[i][j]-1] = cdir

    for i in range(n):
        for j in range(n):
            grid[i][j] = 0
            l = len(tmp[i][j])
            if l == 0:
                continue
            elif l == 1:
                grid[i][j] = tmp[i][j][0]
            else:
                grid[i][j] = min(tmp[i][j])

    #냄새 제거하기, 풍기기
    result = 0
    for i in range(n):
        for j in range(n):
            if frag[i][j][1] == 1:
                frag[i][j] = [0,0]
            else:
                frag[i][j][1] -= 1
            if grid[i][j] != 0:
                result += 1
                frag[i][j] = [grid[i][j],k]
    if result == 1:
        break
    if time == 1000:
        time = -1
        break

print(time)
