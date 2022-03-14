from collections import deque
N, M = map(int, input().split())
virus = []
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 2:
            virus.append([i,j])
    arr.append(tmp)

max_safe = 0

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def find_safe(a):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 0:
                cnt += 1
    return cnt

def in_range(r, c):
    if 0<=r<N and 0<=c<M:
        return 1
    return 0

def bfs(arr):
    for vpos in virus:
        queue = deque()
        queue.append([vpos[0], vpos[1]])
        visited = [[False for _ in range(M)] for _ in range(N)]
        while queue:
            vr, vc = queue.popleft()
            for i in range(4):
                nr,nc = vr + dr[i], vc + dc[i]
                if in_range(nr,nc) and visited[nr][nc] == False and arr[nr][nc] == 0:
                    arr[nr][nc] = 2
                    queue.append([nr,nc])
                    visited[nr][nc] = True
    return arr


tmp = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        tmp[i][j] = arr[i][j]

for fr in range(N):
    for fc in range(M):
        for sr in range(N):
            for sc in range(M):
                for tr in range(N):
                    for tc in range(M):
                        # 벽 세우기
                        if fr == sr and fc == sc:
                            continue
                        if fr == tr and fc == tc:
                            continue
                        if sr == tr and sc == tc:
                            continue
                        if arr[fr][fc] != 0 or arr[sr][sc] != 0 or arr[tr][tc] != 0:
                            continue

                        arr[fr][fc] = 1
                        arr[sr][sc] = 1
                        arr[tr][tc] = 1

                        # bfs
                        arr = bfs(arr)

                        # 최대 안전 영역 크기 구하기
                        max_safe = max(max_safe, find_safe(arr))

                        # 원상복귀
                        for i in range(N):
                            for j in range(M):
                                arr[i][j] = tmp[i][j]

print(max_safe)

# 벽은 다른 위치에 세워야 함.
