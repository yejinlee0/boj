from collections import deque

row, col = map(int, input().split())
arr = [list(map(int, input())) for _ in range(row)]
visited = [[0]*col for _ in range(row)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
# 상 오 하 왼

queue = deque([[0,0]])
while queue:
    r,c = queue.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nc>= 0 and nr < row and nc < col:
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = 1
                arr[nr][nc] = arr[r][c] + 1

print(arr[row-1][col-1])


