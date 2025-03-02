import sys
sys.stdin = open("input.txt", "r")

###########################################################
import itertools
from collections import deque
dxy = ((1,0),(-1,0),(0,1),(0,-1))

def bfs(arr,green):
    visited_color = [[0]*m for _ in range(n)]
    visited_depth = [[0]*m for _ in range(n)]
    q = deque()
    cnt = 0
    for x,y in arr:
        if (x,y) in green:
            q.append((x,y,1,0))
            visited_color[x][y] = 1
            visited_depth[x][y] = 0
        else:
            q.append((x,y,2,0))
            visited_color[x][y] = 2
            visited_depth[x][y] = 0
    while q:
        x,y,c,depth = q.popleft()
        if visited_color[x][y] == 3:
            continue
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<n and 0<=ny<m):
                continue

            if gardens[nx][ny] == 0:
                continue

            if visited_color[nx][ny] in [1,2] and visited_color[nx][ny] != c and visited_depth[nx][ny] == depth+1:
                cnt += 1
                visited_color[nx][ny] = 3

            if visited_color[nx][ny]:
                continue

            visited_depth[nx][ny] = depth + 1
            visited_color[nx][ny] = c
            q.append((nx,ny,c,depth+1))
    return cnt

n,m,g,r = map(int,input().split())
gardens = [list(map(int,input().split())) for _ in range(n)]
# 0 은 호수 1 은 뿌릴수 없음 2 는 뿌릴 수 있음
possible = [(i,j) for i in range(n) for j in range(m) if gardens[i][j] == 2]
result = 0
cache = {}
for per in itertools.combinations(possible,g+r):
    for arr in itertools.combinations(per,g):
        result = max(result, bfs(per, arr))

print(result)
