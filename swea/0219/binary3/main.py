import sys
sys.stdin = open('input.txt', 'r')
##################################################
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m = map(int,input().split())
    b = 0
    for i in range(n):
        b = (b<<1) | 1

    if b & m == b:
        result_str = 'ON'
    else:
        result_str = 'OFF'
    print(f'#{tc} {result_str}')