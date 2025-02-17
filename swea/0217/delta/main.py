import sys
sys.stdin = open('input.txt', 'r')
##################################################
dx = [0,0,1,-1]
dy = [1,-1,0,0]
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    hap = 0
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if not(0 <= nx < n and 0 <= ny < n):
                    continue
                hap += abs(arr[i][j] - arr[nx][ny])
    print(f'#{tc} {hap}')

