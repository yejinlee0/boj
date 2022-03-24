arr = [list(map(int, input())) for _ in range(4)]
k = int(input())
rotate = [list(map(int,input().split())) for _ in range(k)]

# N극 0, S극 1

for num, dir in rotate:
    tmp = [0,0,0,0]
    tmp[num-1] = dir
    if num-1 > 0:
        for i in range(num-2,-1,-1):
            if arr[i][2] == arr[i+1][6]:
                break
            tmp[i] = (-1)*(tmp[i+1])
    if num-1 < 3:
        for i in range(num,4):
            if arr[i-1][2] == arr[i][6]:
                break
            tmp[i] = (-1)*(tmp[i-1])

    for i in range(4):
        if tmp[i] == 1:
            val = arr[i][7]
            for j in range(7,0,-1):
                arr[i][j] = arr[i][j-1]
            arr[i][0] = val
        elif tmp[i] == -1:
            val = arr[i][0]
            for j in range(0,7):
                arr[i][j] = arr[i][j+1]
            arr[i][7] = val

result = 0
if arr[0][0] == 1:
    result += 1
if arr[1][0] == 1:
    result += 2
if arr[2][0] == 1:
    result += 4
if arr[3][0] == 1:
    result += 8

print(result)
