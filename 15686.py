n, m = map(int, input().split())
house = []
chicken = []
grid = [list(map(int, input().split())) for _ in range(n)]
h_cnt = 0
c_cnt = 0
result = 1000000
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            house.append([i,j])
            h_cnt += 1
        elif grid[i][j] == 2:
            chicken.append([i,j])
            c_cnt += 1

def dfs(now, idx, arr):
    global result

    if idx == c_cnt:
        return
    if now == m:
        return

    for k in range(idx,c_cnt):
        arr.append(k)
        dist = 0
        for i in range(h_cnt):
            hr, hc = house[i]
            min_val = 1000000
            for j in arr:
                cr, cc = chicken[j]
                tmp = abs(hr - cr) + abs(hc - cc)
                min_val = min(min_val, tmp)
            dist += min_val
        result = min(result, dist)
        dfs(len(arr),k+1,arr)
        arr.pop()
    return

arr = []
dfs(0,0,arr)

print(result)
