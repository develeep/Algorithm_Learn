import sys

sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

dxy = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    arr[x][y] = 0
    while q:
        px, py = q.popleft()
        for dx,dy in dxy:
            nx,ny = px + dx , py + dy
            if not(0<=nx<n and 0<=ny<m):
                continue
            if arr[nx][ny] == 0:
                continue
            arr[nx][ny] = 0
            q.append((nx,ny))

T = int(input())  # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    points = []
    result_cnt = 0
    for _ in range(k):
        px, py = map(int, input().split())
        arr[px][py] = 1
        points.append((px, py))

    for px, py in points:
        if arr[px][py]:
            result_cnt += 1
            bfs(px, py)

    print(result_cnt)