import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque
dxy = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

def bfs(start,end):
    q = deque()
    q.append((start,0))
    while q:
        (x, y), depth = q.popleft()
        for dx, dy in dxy:
            nx,ny = dx+x, dy+y
            if not(0<= nx < n and 0<=ny<n):
                continue
            if board[nx][ny]:
                continue
            if (nx, ny) == end:
                return depth+1
            board[nx][ny] = 1
            q.append(((nx,ny),depth + 1))
    return 0

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    start, end = [tuple(map(int,input().split())) for _ in range(2)]
    board = [[0]*n for _ in range(n)]
    board[start[0]][start[1]] = 1
    result = bfs(start,end)
    print(result)