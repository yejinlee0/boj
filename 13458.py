N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for students in A:
    if students >= B:
        tmp = students - B
        if tmp % C:
            result += ((tmp//C)+1)
        else:
            result += (tmp//C)
print(result+N)

