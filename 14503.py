import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
dr = [-1,0,1,0] # 북 동 남 서
dc = [0,1,0,-1]
flag = 0

while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        result += 1

    d = (d - 1 + 4) % 4

    r = r + dr[d]
    c = c + dc[d]

    if arr[r][c] == 0:
        continue

    r, c = r - dr[d], c - dc[d]
    flag=0
    for i in range(1,4):
        nd = (d - i + 4) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]

        if (0 > nr or nr >= N) or (0 > nc or nc >= M):
            continue

        if arr[nr][nc] == 0:
            r = nr
            c = nc
            d = nd
            flag=1
            break
    if flag==1:
        continue
    d = nd
    r = r - dr[d]
    c = c - dc[d]
    if 0<=r<N and 0<=c<M and arr[r][c]!=1:
        continue
    break

print(result)
