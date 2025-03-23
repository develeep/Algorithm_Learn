import sys
sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

max_height = max((s for arr in grid for s in arr))

def fill(h):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == h:
                grid[i][j] = 0

dxy = ((0,1),(0,-1),(1,0),(-1,0))
def bfs(x,y, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<n and 0<=ny<n):
                continue
            if visited[nx][ny] or grid[nx][ny] == 0:
                continue
            visited[nx][ny] = 1
            q.append((nx,ny))
def count():
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] and visited[i][j] == 0:
                bfs(i,j, visited)
                cnt += 1

    return cnt

res = 1
for h in range(1, max_height):
    fill(h)
    res = max(res, count())

print(res)