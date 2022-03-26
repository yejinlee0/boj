n,m,t = map(int,input().split())
grid = [[0 for _ in range(m)] for _ in range(n+1)]
for i in range(1,n+1):
    grid[i] = list(map(int, input().split()))
turn = [list(map(int, input().split())) for _ in range(t)]

move = [[-1,0],[0,-1],[1,0],[0,1]]

def in_range(r,c):
    if 0<r<=n and 0<=c<m:
        return 1
    return 0

for x, d, k in turn:
    for i in range(1,n+1):
        if i % x == 0:
            if d == 0:
                for _ in range(k):
                    tmp = grid[i][m-1]
                    for j in range(m-1,0,-1):
                        grid[i][j] = grid[i][j-1]
                    grid[i][0] = tmp
            elif d == 1:
                for _ in range(k):
                    tmp = grid[i][0]
                    for j in range(0,m-1):
                        grid[i][j] = grid[i][j+1]
                    grid[i][m-1] = tmp

    flag = 0
    idx = []
    for i in range(1,n+1):
        for j in range(m):
            if grid[i][j] != 0:
                check = 0
                for dr, dc in move:
                    nr, nc = i+dr, (j+dc+m)%m
                    if in_range(nr,nc) == 1:
                        if grid[nr][nc] == 0:
                            continue
                        elif grid[nr][nc] == grid[i][j]:
                            flag = 1
                            check = 1
                            idx.append([i,j])
                if check == 1:
                    idx.append([i,j])
    for di, dj in idx:
        grid[di][dj] = 0
    if flag == 0:
        val, cnt = 0, 0
        for i in range(1,n+1):
            for j in range(m):
                if grid[i][j] != 0:
                    val += grid[i][j]
                    cnt += 1
        if cnt == 0:
            break
        val = val / cnt
        for i in range(1,n+1):
            for j in range(m):
                if grid[i][j] != 0:
                    if grid[i][j] > val:
                        grid[i][j] -= 1
                    elif grid[i][j] < val:
                        grid[i][j] += 1

print(sum(sum(grid[i])for i in range(1,n+1)))

# 동시 업데이트, 배열 -> 모든 원소 0인 경우 처리, 종료 조건 
