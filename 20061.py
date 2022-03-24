n = int(input())
block = [list(map(int,input().split())) for _ in range(n)]
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0

for t, r, c in block:
    # blue에 블록 놓기
    if t == 1:
        for i in range(5,-1,-1):
            if blue[r][i] == 0:
                if sum(blue[r][0:i]) != 0:
                    continue
                blue[r][i] = 1
                break

    elif t == 2:
        for i in range(5,0,-1):
            if blue[r][i] == 0 and blue[r][i-1] == 0:
                if sum(blue[r][0:i-1]) != 0:
                    continue
                blue[r][i] = blue[r][i-1] = 1
                break

    elif t == 3:
        for i in range(5,-1,-1):
            if blue[r][i] == 0 and blue[r+1][i] == 0:
                if (sum(blue[r][0:i])+sum(blue[r+1][0:i])) != 0:
                    continue
                blue[r][i] = blue[r+1][i] = 1
                break

    # blue 열 확인
    while True:
        flag = 0
        # 열 삭제
        col = 0
        for i in range(5,-1,-1):
            if blue[0][i] + blue[1][i] + blue[2][i] + blue[3][i] == 4:
                flag = 1
                blue[0][i] = blue[1][i] = blue[2][i] = blue[3][i] = 0
                score += 1
                col = i
                break
        if flag == 0:
            break
        # 내리기
        for i in range(col,0,-1):
            blue[0][i] = blue[0][i-1]
            blue[1][i] = blue[1][i-1]
            blue[2][i] = blue[2][i-1]
            blue[3][i] = blue[3][i-1]

            blue[0][i-1] = 0
            blue[1][i-1] = 0
            blue[2][i-1] = 0
            blue[3][i-1] = 0

    # blue 연한 칸 확인
    cnt = 0
    for i in range(1,-1,-1):
        if blue[0][i] + blue[1][i] + blue[2][i] + blue[3][i] == 0:
            continue
        cnt += 1

    for i in range(5,5-cnt,-1):
        blue[0][i] = blue[1][i] = blue[2][i] = blue[3][i] = 0

    if cnt == 1:
        for i in range(5,0,-1):
            blue[0][i] = blue[0][i-1]
            blue[1][i] = blue[1][i-1]
            blue[2][i] = blue[2][i-1]
            blue[3][i] = blue[3][i-1]

            blue[0][i-1] = 0
            blue[1][i-1] = 0
            blue[2][i-1] = 0
            blue[3][i-1] = 0

    elif cnt == 2:
        for i in range(5,1,-1):
            blue[0][i] = blue[0][i-2]
            blue[1][i] = blue[1][i-2]
            blue[2][i] = blue[2][i-2]
            blue[3][i] = blue[3][i-2]

            blue[0][i-2] = 0
            blue[1][i-2] = 0
            blue[2][i-2] = 0
            blue[3][i-2] = 0

    # green에 블록 놓기
    if t == 1:
        for i in range(5,-1,-1):
            if green[i][c] == 0:
                check = 0
                for j in range(0,i):
                    if green[j][c] != 0:
                        check = 1
                        break
                if check == 1:
                    continue

                green[i][c] = 1
                break

    elif t == 2:
        for i in range(5,-1,-1):
            if green[i][c] == 0 and green[i][c+1] == 0:
                check = 0
                for j in range(0, i):
                    if green[j][c] != 0 or green[j][c+1] != 0:
                        check = 1
                        break
                if check == 1:
                    continue

                green[i][c] = green[i][c+1] = 1
                break

    elif t == 3:
        for i in range(5,0,-1):
            if green[i][c] == 0 and green[i-1][c] == 0:
                check = 0
                for j in range(0, i-1):
                    if green[j][c] != 0:
                        check = 1
                        break
                if check == 1:
                    continue

                green[i][c] = green[i-1][c] = 1
                break

    # green 행 확인
    while True:
        flag = 0
        # 행 삭제
        row = 0
        for i in range(5,-1,-1):
            if green[i][0] + green[i][1] + green[i][2] + green[i][3] == 4:
                flag = 1
                green[i][0] = green[i][1] = green[i][2] = green[i][3] = 0
                score += 1
                row = i
                break
        if flag == 0:
            break
        # 내리기
        for i in range(row,0,-1):
            green[i][0] = green[i-1][0]
            green[i][1] = green[i-1][1]
            green[i][2] = green[i-1][2]
            green[i][3] = green[i-1][3]

            green[i-1][0] = 0
            green[i-1][1] = 0
            green[i-1][2] = 0
            green[i-1][3] = 0

    # green 연한 칸 확인
    cnt = 0
    for i in range(1, -1, -1):
        if green[i][0] + green[i][1] + green[i][2] + green[i][3] == 0:
            continue
        cnt += 1

    for i in range(5, 5 - cnt, -1):
        green[i][0] = green[i][1] = green[i][2] = green[i][3] = 0

    if cnt == 1:
        for i in range(5, 0, -1):
            green[i][0] = green[i - 1][0]
            green[i][1] = green[i - 1][1]
            green[i][2] = green[i - 1][2]
            green[i][3] = green[i - 1][3]

            green[i - 1][0] = 0
            green[i - 1][1] = 0
            green[i - 1][2] = 0
            green[i - 1][3] = 0

    elif cnt == 2:
        for i in range(5, 1, -1):
            green[i][0] = green[i - 2][0]
            green[i][1] = green[i - 2][1]
            green[i][2] = green[i - 2][2]
            green[i][3] = green[i - 2][3]

            green[i - 2][0] = 0
            green[i - 2][1] = 0
            green[i - 2][2] = 0
            green[i - 2][3] = 0

print(score)
print(sum(sum(blue[i]) for i in range(4)) + sum(sum(green[i]) for i in range(6)))
# 리스트의 합(슬라이싱, sum) 주의
