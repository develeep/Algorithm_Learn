import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        for j in range(m):
            value = arr[i][j]
            pang = value
            for direction in range(4):
                for val in range(1,value+1):
                    nx, ny = i + dx[direction] * val, j + dy[direction] * val
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        break
                    pang += arr[nx][ny]
            if result < pang:
                result = pang

    print(f'#{tc} {result}')

