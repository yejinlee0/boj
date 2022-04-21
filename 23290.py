M,S = map(int,input().split())

fishD = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
sharkD = [(-1,0),(0,-1),(1,0),(0,1)]
grid = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
frag = [[0 for _ in range(4)] for _ in range(4)]

for _ in range(M):
    r,c,d = map(int,input().split())
    grid[r-1][c-1][d-1] += 1

sr,sc = map(int,input().split())
sr,sc = sr-1,sc-1

def in_range(r,c):
    return 0<=r<4 and 0<=c<4

def no_shark(r,c):
    if r == sr and c == sc:
        return False
    return True

def move_fish(grid):
    tmp = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(8):
                if grid[i][j][k] == 0:
                    continue
                flag = 0
                for dk in range(8):
                    dir = (k-dk+8)%8
                    nr,nc = i+fishD[dir][0],j+fishD[dir][1]
                    if in_range(nr,nc) and no_shark(nr,nc) and frag[nr][nc] == 0:
                        tmp[nr][nc][dir] += grid[i][j][k]
                        flag = 1
                        break
                if flag == 0:
                    tmp[i][j][k] += grid[i][j][k]
    return tmp

def get_killed_num(d1,d2,d3):
    r,c = sr,sc
    cnt = 0
    visited = []
    for move_dir in [d1,d2,d3]:
        nr,nc = r+sharkD[move_dir][0],c+sharkD[move_dir][1]
        if not in_range(nr,nc):
            return -1
        if [nr,nc] not in visited:
            cnt += sum(grid[nr][nc])
            visited.append([nr,nc])
        r,c = nr,nc

    return cnt

def move_shark():
    global sr, sc
    max_cnt = -1
    best_route = [-1,-1,-1]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                m_cnt = get_killed_num(i,j,k)
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = [i,j,k]

    for move_dir in best_route:
        sr,sc = sr+sharkD[move_dir][0],sc+sharkD[move_dir][1]
        if sum(grid[sr][sc]) != 0:
            grid[sr][sc] = [0,0,0,0,0,0,0,0]
            frag[sr][sc] = 3
    return

for turn in range(S):
    ctmp = [[[grid[i][j][k] for k in range(8)] for j in range(4)] for i in range(4)]
    grid = move_fish(grid)

    move_shark()

    for i in range(4):
        for j in range(4):
            if frag[i][j] > 0:
                frag[i][j] -= 1
            for k in range(8):
                grid[i][j][k] += ctmp[i][j][k]

M = 0
for i in range(4):
    for j in range(4):
        M += sum(grid[i][j])
print(M)
# continue, break 시 놓치는 부분 없는 
