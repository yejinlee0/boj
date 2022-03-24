from collections import deque
n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

move_dir = [[-1,0],[0,-1],[1,0],[0,1]]

def check_union(cr,cc,nr,nc):
    people = abs(A[nr][nc] - A[cr][cc])
    if l<=people<=r:
        return 1
    return 0

def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return 1
    return 0

def bfs(r,c,visited):
    union = [[r,c]]
    queue = deque()
    queue.append([r,c])
    visited[r][c] = True
    cnt = 1
    result = A[r][c]
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr+move_dir[i][0], cc+move_dir[i][1]
            if in_range(nr,nc) == 1 and visited[nr][nc] == False and check_union(cr,cc,nr,nc) == 1:
                visited[nr][nc] = True
                queue.append([nr,nc])
                union.append([nr,nc])
                cnt += 1
                result += A[nr][nc]

    return union, cnt, result//cnt

locked = [[False for _ in range(n)] for _ in range(n)]
day = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    all_union = []

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and locked[i][j] == False:
                visited[i][j] = True
                locked[i][j] = True
                tmp_union, tmp, res = bfs(i,j,visited)
                if tmp == 1:
                    continue
                all_union.append([res,tmp,tmp_union])

    if len(all_union) == 0:
        break

    for val, num, union_arr in all_union:
        for i in range(num):
            locked[union_arr[i][0]][union_arr[i][1]] = False
            A[union_arr[i][0]][union_arr[i][1]] = val

    day += 1

print(day)
