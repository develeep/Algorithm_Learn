import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
def find_start():
    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                return (i,j)

dxy = ((-1,0),(1,0),(0,-1),(0,1))

def bfs(xy):
    x, y = xy
    q = deque()
    q.append((x,y,0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x,y,depth = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not (0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] or miro[nx][ny] == 1:
                continue

            if miro[nx][ny] == 3:
                return depth
            visited[nx][ny] = 1

            q.append((nx,ny,depth+1))
    return 0

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    miro = [[int(s) for s in input()] for _ in range(n)]
    print(f'#{tc}',bfs(find_start()))