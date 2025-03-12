import sys
sys.stdin = open('input.txt', 'r')
########################################

def dfs(i,height):
    global res
    if height >= b:
        res = min(res,height)
        return
    if i < n:
        dfs(i+1, height + keys[i])
        dfs(i+1, height)


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,b = map(int,input().split())
    keys = list(map(int,input().split()))
    res = 2000000
    dfs(0,0)
    print(f'#{tc}', res-b)