import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
n, m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxy = ((0,1),(0,-1),(-1,0),(1,0))
def bfs(x,y):
    q = deque()
    q.append((x,y,0))
    while q:
        x,y,depth = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not (0<=nx<n and 0<=ny<m):
                continue
            if visited[nx][ny] or grid[nx][ny] == 0:
                continue
            visited[nx][ny] = depth + 1
            q.append((nx,ny,depth+1))

flag = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            visited[i][j] = 1
            bfs(i,j)
            visited[i][j] = 0
            flag = 1
            break
    if flag:
        break

for i in range(n):
    for j in range(m):
        if grid[i][j] and visited[i][j] == 0 and grid[i][j] != 2:
            visited[i][j] = -1

print('\n'.join(map(lambda x: ' '.join(map(str, x)), visited)))
