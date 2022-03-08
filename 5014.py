from collections import deque
N, start, dest, up, down = map(int, input().split())

arr = [0] * (N+1)
time = 0
queue = deque()
queue.append([start, time])
flag = 0

while queue:
    ns, ntime = queue.popleft()
    if ns == dest:
        time = ntime
        flag = 1
        break
    ntime += 1
    if 1<=ns+up<=N and arr[ns+up] == 0:
        queue.append([ns+up, ntime])
        arr[ns+up] = ntime
    if 1<=ns-down<=N and arr[ns-down] == 0:
        queue.append([ns-down, ntime])
        arr[ns-down] = ntime

if flag == 1:
    print(time)
else:
    print("use the stairs")
