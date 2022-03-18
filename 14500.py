n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(r,c):
    if 0<=r<n and 0<=c<m:
        return 1
    return 0

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(r,c,cnt,tmp):
    global result
    if result >= tmp + max_val * (3 - cnt):
        return
    if cnt == 3:
        result = max(result, tmp)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if in_range(nr,nc) == 1 and visited[nr][nc] == False:
            if cnt == 1:
                visited[nr][nc] = True
                dfs(r,c,cnt+1,tmp+paper[nr][nc])
                visited[nr][nc] = False
            visited[nr][nc] = True
            dfs(nr,nc,cnt+1,tmp+paper[nr][nc])
            visited[nr][nc] = False

    return

result = 0
max_val = max(map(max,paper))
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,0,paper[i][j])
        visited[i][j] = False

print(result)

'''
#시간 
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
t = [
    [[1,1,1,1],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],

    [[1,1,0,0],
     [1,1,0,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,0,0,0],
     [1,0,0,0],
     [1,1,0,0],
     [0,0,0,0]],

    [[1,1,1,0],
     [1,0,0,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,1,0,0],
     [0,1,0,0],
     [0,1,0,0],
     [0,0,0,0]],

    [[0,0,1,0],
     [1,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[0,1,0,0],
     [0,1,0,0],
     [1,1,0,0],
     [0,0,0,0]],

    [[1,0,0,0],
     [1,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,1,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [0,0,0,0]],

    [[1,1,1,0],
     [0,0,1,0],
     [0,0,0,0],
     [0,0,0,0]],

     [[1,0,0,0],
      [1,1,0,0],
      [0,1,0,0],
      [0,0,0,0]],

     [[0,1,1,0],
      [1,1,0,0],
      [0,0,0,0],
      [0,0,0,0]],

     [[0,1,0,0],
      [1,1,0,0],
      [1,0,0,0],
      [0,0,0,0]],

     [[1,1,0,0],
      [0,1,1,0],
      [0,0,0,0],
      [0,0,0,0]],

    [[1,1,1,0],
     [0,1,0,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[0,1,0,0],
     [1,1,0,0],
     [0,1,0,0],
     [0,0,0,0]],

    [[0,1,0,0],
     [1,1,1,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,0,0,0],
     [1,1,0,0],
     [1,0,0,0],
     [0,0,0,0]]
]

def in_range(r, c):
    if 0<=r<n and 0<=c<m:
        return 1
    return 0

result = 0

for i in range(n):
    for j in range(m):
        for e in t:
            tmp = sum([
                paper[i+dr][j+dc]
                for dr in range(4)
                for dc in range(4)
                if in_range(i+dr,j+dc) == 1 and e[dr][dc] == 1
            ])
            result = max(result, tmp)
print(result)
'''
