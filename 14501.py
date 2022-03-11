N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

dp_table = [0 for _ in range(N+1)]
dp_table[N] = 0

for i in range(N-1,-1,-1):
    if i + arr[i][0] < N+1:
        dp_table[i] = max(dp_table[i+1], arr[i][1] + dp_table[i+arr[i][0]])
    else:
        dp_table[i] = dp_table[i+1]

print(dp_table[0])

# 다이나믹 프로그래밍
