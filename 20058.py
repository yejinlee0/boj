from collections import deque
n, q = map(int, input().split())
size = 2**n

a = [list(map(int, input().split())) for _ in range(size)]
l = list(map(int, input().split()))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

ice = 0
result = 0

def in_range(r,c):
    if 0<=r<size and 0<=c<size:
        return 1
    return 0

def count_ice(i,j,visited,tmp):
    cnt = 1
    queue = deque()
    queue.append([i,j])
    visited[i][j] = True

    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if in_range(nr,nc) == 1 and visited[nr][nc] == False and tmp[nr][nc] > 0:
                visited[nr][nc] = True
                queue.append([nr,nc])
                cnt += 1

    return visited, cnt

for ele in l:
    result = 0
    sub_size = 2**ele
    if sub_size == 1:
        tmp = [[a[i][j] for j in range(size)] for i in range(size)]
    else:
        tmp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                for r in range(sub_size):
                    for c in range(sub_size):
                        tmp[i + r][j + c] = a[i + sub_size - c - 1][j + r]

    a = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            cnt = 0
            result += tmp[i][j]
            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                if in_range(nr,nc) == 1 and tmp[nr][nc] > 0:
                    cnt += 1
            if cnt < 3 and tmp[i][j] > 0:
                a[i][j] = tmp[i][j] - 1
                result -= 1
            else:
                a[i][j] = tmp[i][j]

visited = [[False for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        if visited[i][j] == False and a[i][j] > 0:
            visited, tmp_ice = count_ice(i,j,visited,a)
            if tmp_ice > ice:
                ice = tmp_ice

print(result)
print(ice)
#시간초과. PyPy3으로 제출.
