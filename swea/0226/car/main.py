import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    deep_arr = [[int(i) for i in input()] for _ in range(n)]
    move_history = [[float('inf')]*n for _ in range(n)]
    move_history[0][0] = 0

    move_que = deque([(0,0)])
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]

    while len(move_que) > 0:
        x,y = move_que.popleft()
        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            move_cnt = move_history[x][y] + deep_arr[nx][ny]
            if move_cnt < move_history[nx][ny]:
                move_history[nx][ny] = move_cnt
                move_que.append((nx,ny))

    print(f'#{tc}', move_history[n-1][n-1])