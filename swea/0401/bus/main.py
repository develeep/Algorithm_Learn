import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def f(idx, power, cnt):
    global res
    if cnt > res:
        return
    if idx + power >= n-1:
        res = min(res,cnt)
        return
    if powers[idx] > power or power == 0:
        f(idx + 1, powers[idx] - 1, cnt + 1)
    if power > 0:
        f(idx + 1, power - 1, cnt)
T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n, *powers = map(int,input().split())
    res = n
    f(1,powers[0] - 1, 0)
    print(f'#{tc}', res)