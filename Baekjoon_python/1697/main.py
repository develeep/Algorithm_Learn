import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

n,m = map(int,input().split())
visited = [0]*100001
que = deque()
que.append((n,0))

while que:
    x,t = que.popleft()
    if x == m:
        break
    for i in range(3):
        if i == 0:
            nx = x+1
        elif i == 1:
            nx = x-1
        elif i == 2:
            nx = x*2

        if not(0 <= nx <= 100000):
            continue
        if visited[nx]:
            continue
        visited[nx] = 1
        que.append((nx,t+1))

print(t)