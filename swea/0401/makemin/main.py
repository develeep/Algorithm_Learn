import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def dfs(idx, hap):
    global res
    if hap > res:
        return
    if idx == n:
        res = min(res, hap)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(idx + 1, hap + grid[idx][i])
        visited[i] = 0

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    grid = tuple(tuple(map(int,input().split())) for _ in range(n))
    res = float('inf')
    visited = [0]*n
    dfs(0,0)
    print(f'#{tc}', res)