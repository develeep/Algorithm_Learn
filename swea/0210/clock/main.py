import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    dx = [0,1,1]
    dy = [1,1,0]
    result = [['']*3 for _ in range(n)]

    for r in range(n):
        for c in range(3):
            for j in range(n):

                nx = r + (n-1-2*r)*dx[c]
                ny = j + (n-1-2*j)*dy[c]
                if c == 1:
                    result[r][c] += arr[nx][ny]
                    continue
                result[r][c] += arr[ny][nx]

    print(f'#{tc}')
    for _ in result:
        print(*_,sep=" ")