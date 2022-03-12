n = int(input())
arr = [[0]*n for _ in range(n)]
pos = [[-1,-1] for _ in range(n*n+1)]
pref = {}

for _ in range(n*n):
    t1,t2,t3,t4,t5 = map(int, input().split())
    pref[t1] = [t2,t3,t4,t5]

for i, key in enumerate(pref):
    possible = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] != 0:
                continue
            frd, bin = 0, 0
            if 0 <= r + 1 < n:
                if arr[r+1][c] == 0:
                    bin += 1
                elif arr[r+1][c] in pref[key]:
                    frd += 1
            if 0 <= r - 1 < n:
                if arr[r-1][c] == 0:
                    bin += 1
                elif arr[r-1][c] in pref[key]:
                    frd += 1
            if 0 <= c + 1 < n:
                if arr[r][c+1] == 0:
                    bin += 1
                elif arr[r][c+1] in pref[key]:
                    frd += 1
            if 0 <= c - 1 < n:
                if arr[r][c-1] == 0:
                    bin += 1
                elif arr[r][c-1] in pref[key]:
                    frd += 1
            possible.append([frd,bin,r,c])
    possible.sort(key = lambda x:(-x[0],-x[1],x[2],x[3]))
    arr[possible[0][2]][possible[0][3]] = key
    pos[key][0], pos[key][1] = possible[0][2],possible[0][3]

point = 0
for i, key in enumerate(pref):
    r,c = pos[key]
    tmp = []

    if 0 <= r+1 < n: tmp.append(arr[r+1][c])
    if 0 <= r-1 < n: tmp.append(arr[r-1][c])
    if 0 <= c+1 < n: tmp.append(arr[r][c+1])
    if 0 <= c-1 < n: tmp.append(arr[r][c-1])

    res = set(pref[key]) & set(tmp)
    cnt = len(res)

    if cnt > 0:
        point = point + 10**(cnt-1)

print(point)
