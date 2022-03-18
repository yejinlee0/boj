n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
half = n // 2
min_s = 100 * half - 1 * half + 5
total_team = set(range(0,n))
def dfs(cnt, now, arr):
    global min_s, total_team
    if cnt == half:
        start, link = 0, 0
        sarr = set(arr)
        larr = list(total_team - sarr)
        for i in range(half):
            for j in range(i + 1,half):
                start += s[arr[i]][arr[j]] + s[arr[j]][arr[i]]
                link += s[larr[i]][larr[j]] + s[larr[j]][larr[i]]

        tmp = abs(start - link)
        if tmp < min_s:
            min_s = tmp
        return

    for i in range(now, n):
        if i in arr:
            continue
        arr.append(i)
        dfs(cnt+1, i, arr)
        arr.pop(-1)
    return

arr = []
dfs(0,0, arr)
print(min_s)

#집합 사용(차집합)
