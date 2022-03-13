n = int(input())
dust = [list(map(int, input().split())) for _ in range(n)]
r = c = n//2

dr = [0,1,0,-1]
dc = [-1,0,1,0]

# a = (2,1)
grid = [
    [
        [0,  0, 2, 0, 0],
        [0, 10, 7, 1, 0],
        [5,  0, 0, 0, 0],
        [0, 10, 7, 1, 0],
        [0,  0, 2, 0, 0],
    ],
    [
        [0,  0, 0,  0, 0],
        [0,  1, 0,  1, 0],
        [2,  7, 0,  7, 2],
        [0, 10, 0, 10, 0],
        [0,  0, 5,  0, 0],
    ],
    [
        [0, 0, 2,  0, 0],
        [0, 1, 7, 10, 0],
        [0, 0, 0,  0, 5],
        [0, 1, 7, 10, 0],
        [0, 0, 2,  0, 0],
    ],
    [
        [0,  0, 5,  0, 0],
        [0, 10, 0, 10, 0],
        [2,  7, 0,  7, 2],
        [0,  1, 0,  1, 0],
        [0,  0, 0,  0, 0],
    ]
]

idx = 0
weight = 1
iter = 0
result = 0

while not (not r and not c):
    for _ in range(weight):
        pr, pc = r, c
        r = r + dr[idx]
        c = c + dc[idx]
        next_dust = dust[r][c]
        sum_dust = 0
        for i in range(-2,3):
            for j in range(-2,3):
                if grid[idx][2+i][2+j] != 0:
                    tmp = int(next_dust * grid[idx][2+i][2+j] * 0.01)
                    if 0<=r+i<n and 0<=c+j<n:
                        dust[r+i][c+j] += tmp
                    else:
                        result += tmp
                    sum_dust += tmp

        ar, ac = r+dr[idx], c+dc[idx]
        remain = next_dust - sum_dust
        if 0<=ar<n and 0<=ac<n:
            dust[ar][ac] += remain
        else:
            result += remain
        dust[r][c] = 0

        if r == 0 and c == 0:
            break

    idx = (idx + 1) % 4
    iter += 1
    if iter%2 == 0:
        weight += 1

print(result)
