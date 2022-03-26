n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
grid = [[0 for _ in range(n)] for _ in range(n)]

result = 20000

def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return 1
    return 0

idx = []
length = 0
for i in range(0,n):
    for j in range(0,n):
        if (i == 0 or i == n-1) and (j == 0 or j == n-1):
            continue
        for d1 in range(1,n-1):
            for d2 in range(1,n-1):
                r1,c1 = i,j
                r2,c2 = i+d1,j-d1
                if in_range(r2,c2) == 0:
                    continue
                r3,c3 = i+d2, j+d2
                if in_range(r3,c3) == 0:
                    continue
                r4,c4 = i+d1+d2, j-d1+d2
                if in_range(r4,c4) == 0:
                    continue
                idx.append([i,j,d1,d2])
                length += 1

for i,j,d1,d2 in idx:
    for r in range(0,i+d1):
        for c in range(0,j+1):
            grid[r][c] = 1
    for r in range(0,i+d2+1):
        for c in range(j+1,n):
            grid[r][c] = 2
    for r in range(i+d1,n):
        for c in range(0,j-d1+d2):
            grid[r][c] = 3
    for r in range(i+d2+1,n):
        for c in range(j-d1+d2,n):
            grid[r][c] = 4

    for dr in range(d1+1):
        nr, nc = i+1*dr, j-1*dr
        for dc in range(d2+1):
            grid[nr][nc] = 5
            nr,nc = nr+1, nc+1

    rr1, cc1 = i+1, j
    for dr in range(d1):
        nr, nc = rr1+1*dr, cc1-1*dr
        for dc in range(d2):
            grid[nr][nc] = 5
            nr,nc = nr+1, nc+1

    people = [0, 0, 0, 0, 0]
    for r in range(n):
        for c in range(n):
            people[grid[r][c] - 1] += A[r][c]

    result = min(result, max(people) - min(people))
    grid = [[0 for _ in range(n)] for _ in range(n)]

if result == 20000:
    result = 0
print(result)
