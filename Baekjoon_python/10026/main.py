import sys
sys.stdin = open('input.txt', 'r')
###############################################################
from collections import deque
dxy = ((0,-1),(0,1),(1,0),(-1,0))
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny]:
                continue

            if not colors[grid[nx][ny]]:
                continue
            visited[nx][ny] = 1
            q.append((nx,ny))

n = int(input())
grid = tuple(tuple(s for s in input()) for _ in range(n))
visited = [[0]*n for _ in range(n)]
colors = {'R':0, 'G':0, 'B':0}
cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            colors[grid[i][j]] = 1
            bfs(i,j)
            colors[grid[i][j]] = 0
            cnt1 += 1

cnt2 = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if grid[i][j] == 'B':
                colors['B'] = 1
                bfs(i,j)
                colors['B'] = 0
            else:
                colors['R'] = 1
                colors['G'] = 1
                bfs(i,j)
                colors['R'] = 0
                colors['G'] = 0
            cnt2 += 1

print(cnt1,cnt2)
