N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 0상 1좌 2하 3우
dir = [0,0,0,0,0]
max_block = 0

def rotate(d,pre):
    if d == 0 or d == 4:
        return pre
    new = [[0 for _ in range(N)] for _ in range(N)]
    if d == 1:
        for i in range(N):
            for j in range(N):
                new[j][N-1-i] = pre[i][j]
        return new
    elif d == 2:
        for i in range(N):
            for j in range(N):
                new[N-1-i][N-1-j] = pre[i][j]
        return new
    elif d == 3:
        for i in range(N):
            for j in range(N):
                new[N-1-j][i] = pre[i][j]
        return new
    return pre

def merge(board):
    global max_block
    for d in dir:
        board = rotate(d,board)
        new = [[0 for _ in range(N)] for _ in range(N)]
        for j in range(N):
            now, row = -1, 0
            for i in range(N):
                if board[i][j] == 0:
                    continue
                if now == -1:
                    now = board[i][j]
                elif now == board[i][j]:
                    new[row][j] = now * 2
                    now = -1
                    row += 1
                else:
                    new[row][j] = now
                    now = board[i][j]
                    row += 1
            if now != -1:
                new[row][j] = now
                row += 1
        for i in range(N):
            for j in range(N):
                board[i][j] = new[i][j]
        board = rotate(4-d,board)
    max_block = max(max_block, find_max(board))
    return

def find_max(board):
    return max([board[i][j] for i in range(N) for j in range(N)])

def move(dir):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[i][j]

    merge(board)

    for i in range(N):
        for j in range(N):
            board[i][j] = tmp[i][j]

def dfs(cnt):
    if cnt == 5:
        move(dir)
        return

    for i in range(4):
        dir[cnt] = i
        dfs(cnt + 1)

dfs(0)
print(max_block)
