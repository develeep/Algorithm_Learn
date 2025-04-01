import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def f(idx, hap):
    global res
    if idx == n:
        if hap == k:
            res += 1
        return

    f(idx+1, hap+nums[idx])
    f(idx + 1, hap)

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,k = map(int,input().split())
    nums = tuple(map(int,input().split()))
    res = 0
    f(0,0)
    print(f'#{tc}', res)