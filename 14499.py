N, M, y, x, K = map(int, input().split())
#  북
#서  동
#  남
dice = [0]*6

mmap = [list(map(int, input().split())) for _ in range(N)]

command = list(map(int,input().split()))


dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

mmap[y][x] = dice[3]
for i in range(K):
    x = x + dx[command[i]]
    y = y + dy[command[i]]
    # up 0 / front 1 / right 2 / down 3 / back 4 / left 5
    # 동 1  서 2  북 3  남 4
    if 0<=x<M and 0<=y<N:
        if command[i] == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[0]
        elif command[i] == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[5], dice[0], dice[2], dice[3]
        elif command[i] == 3:
            dice[0], dice[1], dice[3], dice[4] = dice[4], dice[0], dice[1], dice[3]
        elif command[i] == 4:
            dice[0], dice[1], dice[3], dice[4] = dice[1], dice[3], dice[4], dice[0]

        if mmap[y][x] == 0:
            mmap[y][x] = dice[3]
        else:
            dice[3] = mmap[y][x]
            mmap[y][x] = 0

        print(dice[0])
    else:
        x = x - dx[command[i]]
        y = y - dy[command[i]]
