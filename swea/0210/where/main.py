import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    r_cnt = 0
    c_cnt = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                c_cnt += 1
                if j + 1 >= n or not (arr[i][j + 1]):
                    if c_cnt == k:
                        result += 1
                    c_cnt = 0
            if arr[j][i]:
                r_cnt += 1
                if j + 1 >= n or not (arr[j+1][i]):
                    if r_cnt == k:
                        result += 1
                    r_cnt = 0
    print(f'#{tc} {result}')

