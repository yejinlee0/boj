n, m, k = map(int, input().split())

# 0위 / 1오위 / 2오 / 3오아래 / 4아래 / 5왼아래 / 6왼 / 7왼위
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

cur = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y, me, s, d = map(int, input().split())
    cur[x - 1][y - 1].append([me, s, d])

for _ in range(k):
    next = [[[] for _ in range(n)] for _ in range(n)]

    # 모든 원자 이동
    for i in range(n):
        for j in range(n):
            for ele in cur[i][j]:
                s, d = ele[1], ele[2]
                nr = (i + dr[d] * s + n * s) % n
                nc = (j + dc[d] * s + n * s) % n
                next[nr][nc].append(ele)

    # 합성
    cur = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            length = len(next[i][j])
            if length == 1:
                cur[i][j].append(next[i][j][0])
            elif length > 1:
                sum_m, sum_v = 0, 0
                d1, d2 = 0, 0
                for ele in next[i][j]:
                    sum_m += ele[0]
                    sum_v += ele[1]
                    if ele[2] % 2 == 1:
                        d2 += 1
                    else:
                        d1 += 1
                sum_m = sum_m // 5
                if sum_m <= 0:
                    continue
                sum_v = sum_v // length
                if d1 == length or d2 == length:
                    cur[i][j].append([sum_m, sum_v, 0])
                    cur[i][j].append([sum_m, sum_v, 2])
                    cur[i][j].append([sum_m, sum_v, 4])
                    cur[i][j].append([sum_m, sum_v, 6])
                else:
                    cur[i][j].append([sum_m, sum_v, 1])
                    cur[i][j].append([sum_m, sum_v, 3])
                    cur[i][j].append([sum_m, sum_v, 5])
                    cur[i][j].append([sum_m, sum_v, 7])

result = 0
for i in range(n):
    for j in range(n):
        for ele in cur[i][j]:
            result += ele[0]
print(result)

# 알고리즘 다시 확인해보고 틀린 점이 없으면 범위 확인하고 변수 제대로 사용했는지 확인하기
# 이 문제의 경우 ele[2] 대신 d를 사용하는 실수를 했음
# 문제 유형에 따라 각 원소가 리스트형인 2차원 배열을 사용할 수 있음
# 1. 각 리스트에 추가되는 형태 -> 이 문제처럼 2개의 2차원 배열을 사용하면 편리함
# 2. 각 리스트가 방향별로 존재하는 무언가의 수를 담는 형태
