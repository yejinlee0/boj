n,k = map(int,input().split())
move = [(0,1),(0,-1),(-1,0),(1,0)]

grid = [list(map(int,input().split())) for _ in range(n)]
mal = [[[] for _ in range(n)] for _ in range(n)]
info = [(0,0,0)]

max_cnt = 1
for i in range(1,k+1):
    r,c,d = map(int,input().split())
    mal[r-1][c-1] = [i]
    info.append((r-1,c-1,d-1))

def in_range(r,c):
    return 0<=r<n and 0<=c<n

turn = 1
while True:
    for i in range(1,k+1):
        cr,cc,cd = info[i]
        nr,nc = cr+move[cd][0], cc+move[cd][1]

        if in_range(nr,nc) == False or grid[nr][nc] == 2:
            if cd % 2 == 0:
                cd += 1
            else:
                cd -= 1
            nr,nc = cr+move[cd][0], cc+move[cd][1]
            if in_range(nr,nc) == False or grid[nr][nc] == 2:
                info[i] = (cr,cc,cd)
                continue
        tmp = []
        idx = mal[cr][cc].index(i)
        tmp.extend(mal[cr][cc][idx:])
        del mal[cr][cc][idx:]
        info[tmp[0]] = (nr,nc,cd)
        for j in range(1,len(tmp)):
            dd = info[tmp[j]][2]
            info[tmp[j]] = (nr,nc,dd)
        if grid[nr][nc] == 1:
            tmp = tmp[::-1]
        mal[nr][nc].extend(tmp)
        l = len(mal[nr][nc])
        if max_cnt < l:
            max_cnt = l
        if max_cnt >= 4:
            break
    if max_cnt >= 4:
        break
    if turn == 1000:
        turn = -1
        break
    turn += 1

print(turn)
