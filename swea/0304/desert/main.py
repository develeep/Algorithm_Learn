import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
dxy = ((1,1),(1,-1),(-1,-1),(-1,1))
def bfs(x,y,d,depth1,depth2,history):
    global result
    q = deque()
    q.append((x,y,d,depth1,depth2,history))
    history.append(deserts[x][y])
    while q:
        x,y,d,depth1,depth2,history = q.popleft()
        nx,ny = x,y

        while 1:
            nx, ny = nx + dxy[d][0], ny + dxy[d][1]

            if not(0<=nx<n and 0<=ny<n):
                break
            if d == 3:
                depth2 -= 1
                if depth2 == 0:
                    result = max(result, len(history))
                    break

            if deserts[nx][ny] in history:
                break

            history.append(deserts[nx][ny])

            if d == 0:
                depth1 += 1
                q.append((nx,ny,d+1,depth1,depth2,history[:]))
            if d == 1:
                depth2 += 1
                q.append((nx,ny,d+1,depth1,depth2,history[:]))
            if d == 2:
                depth1 -= 1
                if depth1 == 0:
                    q.append((nx,ny,d+1,depth1,depth2,history[:]))




T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    deserts = [list(map(int,input().split())) for _ in range(n)]
    result = -1
    for i in range(n-1):
        for j in range(1,n-1):
            history = []
            res = bfs(i,j,0,0,0,[])

    print(f'#{tc}', result)