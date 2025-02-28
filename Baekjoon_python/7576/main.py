import sys
sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not(0 <= nx < n and 0 <= ny < m):
            continue
        if arr[nx][ny] != 0:
            continue

        arr[nx][ny] += arr[x][y] + 1
        q.append((nx,ny))

result = 0
for row in arr:
    if 0 in row:
        print(-1)
        exit(0)
    result = max(result, max(row))
print(result-1)