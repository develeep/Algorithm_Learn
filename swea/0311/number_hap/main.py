import sys
sys.stdin = open('input.txt', 'r')
########################################
dxy = ((0,1),(0,-1),(-1,0),(1,0))
def dfs(x,y, hap):
    if len(hap) == 7:
        res.add(hap)
        return

    for dx,dy in dxy:
        nx, ny = x+dx, y+dy
        if not(0<=nx<4 and 0<= ny < 4):
            continue

        dfs(nx,ny, hap + arr[nx][ny])


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    res = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j, arr[i][j])
    print(f'#{tc}', len(res))