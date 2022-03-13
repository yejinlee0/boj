n, k = map(int, input().split())
safe = list(map(int, input().split()))
people = [0]*n

cnt = 0
lidx = 2*n - 1
turn = 0

while cnt < k:
    turn += 1
    # 1단계
    last = safe[lidx]
    for i in range(lidx, 0, -1):
        safe[i] = safe[i-1]
    safe[0] = last
    for i in range(n-1, 0, -1):
        people[i] = people[i-1]
    people[0] = 0
    people[n-1] = 0

    # 2단계
    for i in range(n-2, 0, -1):
        if people[i] == 1 and people[i+1] == 0 and safe[i+1] > 0:
            people[i] = 0
            people[i+1] = 1
            safe[i+1] -= 1
            if safe[i+1] == 0:
                cnt+=1

    # 3단계
    if people[0] == 0 and safe[0] > 0:
        people[0] = 1
        safe[0] -= 1
        if safe[0] == 0:
            cnt += 1

    if people[n-1] == 1:
        people[n-1] = 0

print(turn)
# 무빙 워크 위에 사람이 있는 경우에만 사람을 이동시켜야 함
# 전체는 2*n 개가 있지만 실제로 사람이 있을 수 있는 공간은 n 개임
# n 번째에 위치하면 무조건 내려야 함
