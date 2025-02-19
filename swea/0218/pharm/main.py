import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [[int(s) for s in input()] for _ in range(n)]
    start = end = n//2
    flag = 0
    cnt = 0
    x = 1
    for i in range(n):
        for j in range(start,end+1):
            cnt += arr[i][j]
        start -= x
        end += x
        if start == 0:
            x *= -1
    print(f'#{tc} {cnt}')
