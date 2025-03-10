import sys

sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
dxy = ((-1, 0), (1, 0), (0, 1), (0, -1))

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited = [[0] * n for _ in range(n)]
    while que:
        x,y = que.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not (0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] == 1 or maps[nx][ny] == 1:
                continue
            if maps[nx][ny] == 3:
                return 1
            visited[nx][ny] = 1
            que.append((nx,ny))
    return 0

T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input().strip())
    maps = [[int(s) for s in input().strip()] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                res = bfs(i,j)
                break

    print(f'#{tc}', res)
