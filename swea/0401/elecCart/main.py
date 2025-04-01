import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def dfs(idx, old, hap):
    global res
    if hap > res:
        return

    if idx == n:
        hap += grid[old][0]
        res = min(res,hap)
        return

    for i in range(1, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(idx + 1, i, hap + grid[old][i])
        visited[i] = 0

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    grid = tuple(tuple(map(int,input().split())) for _ in range(n))
    visited = [0]*n
    res = float('inf')
    dfs(1, 0, 0)
    print(f'#{tc}', res)