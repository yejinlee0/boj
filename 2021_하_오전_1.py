from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
point = 0

# 시계 방향
# 오른쪽 0 / 아래쪽 1 / 왼쪽 2 / 윗쪽 3
dr = [0,1,0,-1]
dc = [1,0,-1,0]
d = 0
r, c = 0, 0
up, front, right = 1, 2, 3

def bfs(r,c,now):
    result = 1
    queue = deque()
    queue.append([r,c])
    visited = [[False]*n for _ in range(n)]
    visited[r][c] = True
    while queue:
        cr, cc = queue.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0<=nr<n and 0<=nc<n and visited[nr][nc] == False and arr[nr][nc] == now:
                visited[nr][nc] = True
                queue.append([nr,nc])
                result += 1

    return result

for i in range(m):
    r = r + dr[d]
    c = c + dc[d]

    if 0 > r or r >= n or 0 > c or c >= n:
        r = r - dr[d]
        c = c - dc[d]
        d = (d + 2) % 4
        r = r + dr[d]
        c = c + dc[d]

    #주사위 굴리기
    # 오른쪽 0 / 아래쪽 1 / 왼쪽 2 / 윗쪽 3
    if d == 0:
        up, right =  7 - right, up
    elif d == 1:
        up, front = 7 - front, up
    elif d == 2:
        up, right = right, 7 - up
    elif d == 3:
        up, front = front, 7 - up

    # 점수
    now = arr[r][c]
    cnt = bfs(r,c,now)
    point = point + now*cnt

    # 방향
    if 7 - up > now:
        d = (d + 1) % 4
    elif 7 - up < now:
        d = (d + 3) % 4
    # 주사위 반시계 방향 주의하기

print(point)
