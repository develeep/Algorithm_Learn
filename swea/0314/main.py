import sys
sys.stdin = open('input.txt', 'r')
########################################
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,m = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    res  = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                cnt += 1
            if cnt > 0 and (maps[i][j] == 0 or j == (m-1)):
                res = max(res,cnt)
                cnt = 0

    for j in range(m):
        for i in range(n):
            if maps[i][j] == 1:
                cnt += 1
            if cnt > 0 and (maps[i][j] == 0 or i == (n-1)):
                res = max(res,cnt)
                cnt = 0

    print(f'#{tc}', res)