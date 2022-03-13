N = int(input())
A = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
# 0     1    2    3
op = list(map(int, input().split()))

max_n = -1000000001
min_n = 1000000001

def dfs(cnt, value, plus, minus, multiply, divide):
    global max_n, min_n
    if cnt == N-1:
        if value > max_n:
            max_n = value
        if value < min_n:
            min_n = value
        return
    if plus > 0:
        dfs(cnt+1, value+A[cnt+1], plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(cnt+1, value-A[cnt+1], plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(cnt+1, value*A[cnt+1], plus, minus, multiply-1, divide)
    if divide > 0:
        if A[cnt+1] > 0 and value < 0:
            value = (-1)*value
            value = value//A[cnt+1]
            value = (-1)*value
        else:
            value = value//A[cnt+1]
        dfs(cnt+1, value, plus, minus, multiply, divide-1)


dfs(0, A[0], op[0], op[1], op[2], op[3])
print(max_n)
print(min_n)
