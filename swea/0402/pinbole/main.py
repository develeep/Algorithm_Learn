import sys
sys.stdin = open('input.txt', 'r')
###############################################################
# 상하좌우
dxy = ((-1,0),(1,0),(0,-1),(0,1))
walls = ((1,3,0,2),(3,0,1,2),(2,0,3,1),(1,2,3,0))
block = {0:1,1:0,2:3,3:2}

def dfs(x,y,d,cnt):
    history = [(x,y)]
    nx,ny = x,y
    while 1:
        nx, ny = nx + dxy[d][0], ny + dxy[d][1]
        if not(0<=nx<n and 0<=ny<n):
            cnt = (cnt*2) + 1
            break
        if grid[nx][ny] == -1:
            break
        if his[nx][ny][d]:
            cnt += his[nx][ny][d]
            break
        if grid[nx][ny] == 5:
            cnt = (cnt*2) + 1
            break
        if 1 <= grid[nx][ny] < 5:
            change_d = walls[grid[nx][ny] - 1][d]
            if block[change_d] == d:
                cnt = (cnt * 2) + 1
                break
            else:
                cnt = dfs(nx, ny, change_d, 0) + 2
                break
        else:
            history.append((nx,ny))
            if grid[nx][ny] > 5:
                for hole in holes[grid[nx][ny]]:
                    if hole != (nx,ny):
                        nx,ny = hole
                        history.append((nx,ny))
                        break
    for hx,hy in history:
        his[hx][hy][d] = cnt
    return cnt


T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    grid = tuple(tuple(map(int,input().split())) for _ in range(n))
    his = [[[0,0,0,0] for _ in range(n)] for _ in range(n)]
    holes = [[] for _ in range(11)]
    result = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 5:
                holes[grid[i][j]].append((i,j))

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for d in range(4):
                    if his[i][j][d]:
                        continue
                    res = dfs(i,j,d,0)
                    result = max(res,result)
    print(f"#{tc}", result)