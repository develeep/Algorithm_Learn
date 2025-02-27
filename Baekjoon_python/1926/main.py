import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque
n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxy = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1
    size = 0
    while que:
        mx, my = que.popleft()
        size += 1
        for d in range(4):
            nx,ny = mx+dxy[d][0] , my+dxy[d][1]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if arr[nx][ny] == 0 or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            que.append((nx,ny))
    return size

cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            cnt +=1
            max_size = max(max_size, bfs(i,j))

print(cnt)
print(max_size)