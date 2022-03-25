dice = list(map(int, input().split()))
score = 0
grid = [
    0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
    13,16,19,
    22,24,
    28,27,26,
    25,30,35,40,0
]

info = [0,0,0,0]

def next_pos(crt_pos, move):
    if crt_pos == 32:
        return 32
    if move == 0:
        return crt_pos

    if crt_pos in [22,24]:
        next = 28
    elif crt_pos == 19:
        next = 31
    else:
        next = crt_pos + 1

    return next_pos(next,move - 1)

def is_overlapped():
    return any([
        info[i] == info[j] and info[i] != 0 and info[i] != 32
        for i in range(4)
        for j in range(i+1,4)
    ])

def dfs(idx,point):
    global score
    if idx == 10:
        score = max(score,point)
        return

    for i in range(4):
        if info[i] == 32:
            continue
        tmp = info[i]
        now = tmp

        if now == 5:
            info[i] = next_pos(20,dice[idx] - 1)

        elif now == 10:
            info[i] = next_pos(23,dice[idx] - 1)

        elif now == 15:
            info[i] = next_pos(25,dice[idx] - 1)

        else:
            info[i] = next_pos(info[i],dice[idx])

        if info[i] >= 32:
            info[i] = 32

        if not is_overlapped():
            dfs(idx+1,point+grid[info[i]])
        info[i] = tmp

    return

dfs(0,0)
print(score)

# 한 칸씩 움직이기, 복원 주의
