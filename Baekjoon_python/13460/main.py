import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque
n,m = map(int,input().split())
map_arr = [[i for i in input()] for _ in range(n)]


def find_RB():
    red,blue = [],[]

    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == 'R':
                red = [i,j]
            if map_arr[i][j] == 'B':
                blue = [i,j]

    return red,blue

def move(color,d):
    x, y = color
    while map_arr[x][y] != "#":
        nx = x + dx[d]
        ny = y + dy[d]
        if map_arr[nx][ny] == '#':
            return x, y
        if map_arr[nx][ny] == 'O':
            return nx, ny
        x, y = nx, ny
    return x, y



dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 우좌하상

def bfs():
    move_que = deque()
    move_que.append((*find_RB(), 0))
    visited = []
    result = 11
    while move_que:
        red,blue,depth = move_que.popleft()
        if depth == 10:
            break
        visited.append((red,blue))

        for d in range(4):
            if map_arr[red[0]+dx[d]][red[1]+dy[d]] == '#' and map_arr[blue[0]+dx[d]][blue[1]+dy[d]] == '#':
                continue
            rx,ry = move(red,d)
            bx,by = move(blue,d)
            if (rx,ry) != (bx,by):
                if map_arr[rx][ry] == 'O':
                    result = min(result,depth+1)
                    continue
                elif map_arr[bx][by] == 'O':
                    continue
            else:
                if map_arr[rx][ry] == 'O':
                    continue
                # r좌표가 이동하고자 하는 방향에 b 좌표보다 앞에 있는 경우
                if (d == 0 and blue[1] < red[1]) or (d == 1 and blue[1] > red[1]) or (d == 2 and blue[0] < red[0]) or (d == 3 and blue[0] > red[0]):
                    bx -= dx[d]
                    by -= dy[d]
                else:
                    rx -= dx[d]
                    ry -= dy[d]

            if ((rx,ry), (bx,by)) in visited:
                continue

            move_que.append(((rx,ry),(bx,by),depth+1))
    return result if result <= 10 else -1
print(bfs())
