import sys
sys.stdin = open('input.txt', 'r')
###############################################################
# 상하좌우
dxy = ((-1,0),(1,0),(0,-1),(0,1))
walls = ((1,3,0,2),(3,0,1,2),(2,0,3,1),(1,2,3,0))
block = {0:1,1:0,2:3,3:2}

def f(start_x,start_y,d):
    cnt = 0
    direction = d
    x,y = start_x, start_y
    while 1:
        x, y = x + dxy[direction][0], y + dxy[direction][1]
        if (start_x,start_y) == (x,y):
            return cnt

        if not(0<=x<n and 0<=y<n):
            return (cnt*2) + 1
        if grid[x][y] == 0:
            continue
        if grid[x][y] > 5:
            for hole in holes[grid[x][y]]:
                if hole != (x,y):
                    x,y = hole
                    break
            continue
        if grid[x][y] == -1:
            return cnt
        if grid[x][y] == 5:
            return (cnt*2) + 1
        if 1 <= grid[x][y] < 5:
            change_d = walls[grid[x][y] - 1][direction]
            if block[change_d] == direction:
                return (cnt * 2) + 1
            else:
                direction = change_d
                cnt += 1
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
                    res = f(i,j,d)
                    result = max(res,result)
    print(f"#{tc}", result)