import sys
sys.stdin = open('input.txt', 'r')
###############################################################
T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    DP = [0]*n
    DP[0] = 1
    DP[1] = 3
    DP[2] = 6
    for i in range(n):
        if i < 3:
            continue
        DP[i] = DP[i-1] + (DP[i-2] * 2) + DP[i-3]
    print(f'#{tc}', DP[n-1])