import sys
sys.stdin = open('input.txt', 'r')
##################################################
import heapq

n,m = map(int,input().split())
miro = [[int(s) for s in input()] for _ in range(n)]
min_history = [[float('inf')]*m for _ in range(n)]

move_que = []
heapq.heappush(move_que,(1,0,0))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
min_history[0][0] = 1

while move_que:
    depth,x,y = heapq.heappop(move_que)
    if (x,y) == (n-1,m-1):
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not(0 <= nx < n and 0 <= ny < m):
            continue
        if miro[nx][ny] == 0:
            continue
        if min_history[nx][ny] > depth + 1:
            min_history[nx][ny] = depth + 1
            heapq.heappush(move_que,(depth+1,nx,ny))
print(depth)