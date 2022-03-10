from collections import deque
import sys
input = sys.stdin.readline

def bfs(c, r):
    queue = deque()
    queue.append([c,r])
    while queue:
        cc, cr = queue.popleft()
        if abs(cc - festival_x) + abs(cr - festival_y) <= 1000:
            print("happy")
            return
        for i in range(store):
            if not visited[i]:
                nc, nr = store_pos[i]
                if abs(cc - nc) + abs(cr - nr) <= 1000:
                    queue.append([nc,nr])
                    visited[i] = True

    print("sad")
    return

testcase = int(input())
for _ in range(testcase):
    store = int(input())
    house_x, house_y = map(int, input().split())
    store_pos = deque()
    for i in range(store):
        tx, ty = map(int, input().split())
        store_pos.append([tx,ty])
    festival_x, festival_y = map(int, input().split())
    visited = [False for i in range(store)]

    bfs(house_x, house_y)


