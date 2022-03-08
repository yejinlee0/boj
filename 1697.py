from collections import deque

x, y = map(int, input().split())
arr = [0] * 100002
time = 0
queue = deque()
queue.append([x,y,time])

while queue:
    nx, ny, ntime = queue.popleft()
    if nx == ny:
        time = ntime
        break
    ntime += 1
    if 0<=nx-1<=100000 and arr[nx-1] == 0:
        queue.append([nx-1,ny,ntime])
        arr[nx-1] = ntime
    if 0<=nx+1<=100000 and arr[nx+1] == 0:
        queue.append([nx+1,ny,ntime])
        arr[nx+1] = ntime
    if 0<=nx*2<=100000 and arr[2*nx] == 0:
        queue.append([nx*2,ny,ntime])
        arr[nx*2] = ntime

print(time)

# 배열 크기 주의, 모든 것을 자료구조로 변환할 
