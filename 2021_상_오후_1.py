n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
medi = []
medi.append([n-2,0])
medi.append([n-2,1])
medi.append([n-1,0])
medi.append([n-1,1])

# 1오 2오위 3위 4왼위 5왼 6왼아 7아 8오아
dr = [0,-1,-1,-1,0,1,1,1]
dc = [1,1,0,-1,-1,-1,0,1]

for year in range(m):
    cnt = len(medi)
    # 1, 2 단계
    direction, p = move[year][0], move[year][1]
    for i in range(cnt):
        mr, mc = medi[i][0], medi[i][1]
        mr = (mr + dr[direction-1]*p + n*p)%n
        mc = (mc + dc[direction-1]*p + n*p)%n
        arr[mr][mc] += 1
        medi[i][0], medi[i][1] = mr, mc

    # 3 단계
    for i in range(cnt):
        check = 0
        mr, mc = medi[i][0], medi[i][1]
        if 0<=mr-1<n and 0<=mc-1<n and arr[mr-1][mc-1]>=1:
            check += 1
        if 0<=mr-1<n and 0<=mc+1<n and arr[mr-1][mc+1]>=1:
            check += 1
        if 0<=mr+1<n and 0<=mc-1<n and arr[mr+1][mc-1]>=1:
            check += 1
        if 0<=mr+1<n and 0<=mc+1<n and arr[mr+1][mc+1]>=1:
            check += 1
        arr[mr][mc] += check

    # 4 단계
    medi2 = []
    for i in range(n):
        for j in range(n):
            tmp = [i,j]
            if tmp in medi:
                continue
            if arr[i][j] >= 2:
                arr[i][j] -= 2
                medi2.append(tmp)
    medi = list(medi2)

height = 0
for i in range(n):
    for j in range(n):
        height += arr[i][j]
print(height)

# 영양제의 개수는 항상 4개가 아님
