import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    max_result = 0
    for i in range(n):
        for j in range(m):
            hap = arr[i][j]
            for direction in range(4):
                nx = i + dx[direction]
                ny = j + dy[direction]

                if 0 <= nx < n and 0 <= ny < m:
                    hap += arr[nx][ny]
            max_result = max(max_result, hap)

    print(f'#{tc} {max_result}')
