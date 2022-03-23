moves = [[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

shark = [0,0,0] # 방향, 행, 열
fish = [[[0,0] for _ in range(4)] for _ in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))
    fish[i][0] = [tmp[0], tmp[1]]
    fish[i][1] = [tmp[2], tmp[3]]
    fish[i][2] = [tmp[4], tmp[5]]
    fish[i][3] = [tmp[6], tmp[7]]

fish_info = [[0,0,0] for _ in range(17)]

for i in range(4):
    for j in range(4):
        if fish[i][j][0] == 0:
            continue
        fish_info[fish[i][j][0]] = [fish[i][j][1],i,j]

def in_range(r,c):
    if 0<=r<4 and 0<=c<4:
        return 1
    return 0

def same_shark(r,c):
    if shark[1] == r and shark[2] == c:
        return 1
    return 0

def move_fish():
    global fish
    global fish_info
    for i in range(1,17):
        cd, cr, cc = fish_info[i]
        if cd == -1:
            continue
        while True:
            cr, cc = cr + moves[cd][0], cc + moves[cd][1]
            if in_range(cr, cc) == 1 and same_shark(cr, cc) == 0:
                if fish[cr][cc][0] == 0: # 빈칸인 경우
                    fish[cr][cc] = [i, cd]
                    fish[fish_info[i][1]][fish_info[i][2]] = [0, 0]
                    fish_info[i] = [cd, cr, cc]
                else: # 물고기 있는 경우 swap
                    tmp = fish[cr][cc]
                    idx = tmp[0]
                    fish[cr][cc] = [i, cd]
                    fish[fish_info[i][1]][fish_info[i][2]] = tmp

                    fish_info[idx][1], fish_info[idx][2] = fish_info[i][1], fish_info[i][2]
                    fish_info[i] = [cd, cr, cc]
                break
            cr, cc = cr - moves[cd][0], cc - moves[cd][1] ##
            cd = cd - 1
            cd = (cd + 1) % 8 + 1
            if cd == fish_info[i][0]:
                break
    return

def dfs(eat_fish,cnt_fish,shark_info,fnum):
    global max_eat
    global shark, fish, fish_info

    if cnt_fish == 0:
        max_eat = max(max_eat, eat_fish)
        return

    shark[0], shark[1], shark[2] = shark_info
    fish[shark[1]][shark[2]] = [0, 0]
    fish_info[fnum][0] = -1

    move_fish()

    # 먹으면 fish_info 방향 -1로 설정
    sd, sr, sc = shark
    while True:
        sr, sc = sr + moves[sd][0], sc + moves[sd][1]
        if in_range(sr, sc) == 0:
            max_eat = max(max_eat, eat_fish)
            return
        if fish[sr][sc][0] != 0:

            tmp_shark = [shark[0],shark[1],shark[2]]
            tmp_fish = [[[0,0] for _ in range(4)] for _ in range(4)]
            tmp_fish_info = [[0,0,0] for _ in range(17)]

            for i in range(4):
                for j in range(4):
                    tmp_fish[i][j] = [fish[i][j][0],fish[i][j][1]]
                tmp_fish_info[4 * i + 1] = [fish_info[4 * i + 1][0], fish_info[4 * i + 1][1], fish_info[4 * i + 1][2]]
                tmp_fish_info[4 * i + 2] = [fish_info[4 * i + 2][0], fish_info[4 * i + 2][1], fish_info[4 * i + 2][2]]
                tmp_fish_info[4 * i + 3] = [fish_info[4 * i + 3][0], fish_info[4 * i + 3][1], fish_info[4 * i + 3][2]]
                tmp_fish_info[4 * i + 4] = [fish_info[4 * i + 4][0], fish_info[4 * i + 4][1], fish_info[4 * i + 4][2]]

            dfs(eat_fish+fish[sr][sc][0],cnt_fish-1,[fish[sr][sc][1],sr,sc],fish[sr][sc][0])

            shark = [tmp_shark[0],tmp_shark[1],tmp_shark[2]]

            for i in range(4):
                for j in range(4):
                    fish[i][j] = [tmp_fish[i][j][0],tmp_fish[i][j][1]]

                fish_info[4 * i + 1] = [tmp_fish_info[4 * i + 1][0], tmp_fish_info[4 * i + 1][1], tmp_fish_info[4 * i + 1][2]]
                fish_info[4 * i + 2] = [tmp_fish_info[4 * i + 2][0], tmp_fish_info[4 * i + 2][1], tmp_fish_info[4 * i + 2][2]]
                fish_info[4 * i + 3] = [tmp_fish_info[4 * i + 3][0], tmp_fish_info[4 * i + 3][1], tmp_fish_info[4 * i + 3][2]]
                fish_info[4 * i + 4] = [tmp_fish_info[4 * i + 4][0], tmp_fish_info[4 * i + 4][1], tmp_fish_info[4 * i + 4][2]]

    return

max_eat = fish[0][0][0]

dfs(max_eat,15,[fish[0][0][1],0,0],max_eat)

print(max_eat)

# 백트래킹, 원래 배열 저장 -> dfs -> 복원, 방향 탐색시 복원 주의
