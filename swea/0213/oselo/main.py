import sys
sys.stdin = open('input.txt', 'r')
##################################################
dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
T = int(input())  # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    board = [[0] * n for _ in range(n)]
    center = n // 2
    board[center - 1][center - 1], board[center - 1][center], board[center][center - 1], board[center][
        center] = 2, 1, 1, 2

    for x, y, user in arr:
        board[x - 1][y - 1] = user
        for i in range(len(dx)):
            j = 1
            while 1:
                nx = x - 1 + dx[i] * j
                ny = y - 1 + dy[i] * j

                if not (0 <= nx < n and 0 <= ny < n and board[nx][ny]):
                    break
                if board[nx][ny] == user:
                    for idx in range(1, j + 1):
                        nx = x - 1 + dx[i] * idx
                        ny = y - 1 + dy[i] * idx
                        board[nx][ny] = user
                    break
                j += 1

    result = [x for b in board for x in b]
    a = result.count(1)
    b = result.count(2)
    print(f'#{tc} {a} {b}')