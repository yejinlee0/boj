#0부터 인덱스 주의
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]

N, M = map(int, input().split())
bascket = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]

def in_range(r, c):
    if 0<=r<N and 0<=c<N:
        return 1
    return 0

for turn in range(M):
    di, si = move[turn]
    new_cloud = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for ele_cloud in cloud:
        r, c = ele_cloud
        nr, nc = (r + dr[di-1]*si + N*si)%N, (c + dc[di-1]*si + N*si)%N
        new_cloud.append([nr,nc])
        bascket[nr][nc] += 1
        visited[nr][nc] = True

    for ele_cloud in new_cloud:
        r, c = ele_cloud
        cnt = 0
        for i in range(4):
            idx = 2*i + 1
            nr, nc = r+dr[idx], c+dc[idx]
            if in_range(nr,nc) and bascket[nr][nc] > 0:
                cnt += 1
        bascket[r][c] += cnt

    cloud = []
    for i in range(N):
        for j in range(N):
            if bascket[i][j] >= 2 and visited[i][j] == False:
                bascket[i][j] -= 2
                cloud.append([i,j])

result = 0
for i in range(N):
    for j in range(N):
        result += bascket[i][j]

print(result)
# 시간 초과 해결 : 메모리를 써서 visited로 확인 방법으로 수정함
