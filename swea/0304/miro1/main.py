import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
def find_start():
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                return i,j
    return 1,1

dxy = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(x,y):
    visited = [[0]*n for _ in range(n)]
    q = deque([(x,y)])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] or miro[nx][ny]:
                if miro[nx][ny] == 3:
                    return 1
                continue
            visited[nx][ny] = 1
            q.append((nx,ny))
    return 0

T = 1     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    t = int(input())

    n = 100
    miro = [[int(s) for s in input().strip()] for _ in range(n)]
    x,y = find_start()
    res = bfs(x,y)
    print(f'#{t}', res)
