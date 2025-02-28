import sys
<<<<<<< HEAD
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
=======

sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque


def validate(s):
    if s == '.':
        return 0
    if s == '#':
        return 100
    if s == 'R':
        return 1
    if s == 'B':
        return 2
    if s == 'O':
        return 5


def red_move(d, rx, ry):
    global map_arr
    x, y = rx, ry
    while 1:
        nx = x + dxy[d][0]
        ny = y + dxy[d][1]
        if map_arr[nx][ny] == 5:
            map_arr[x][y] = 0
            return nx, ny
        if map_arr[nx][ny] == 0:
            map_arr[x][y], map_arr[nx][ny] = map_arr[nx][ny], map_arr[x][y]
            x, y = nx, ny
        else:
            break
    return x, y


def blue_move(d, bx, by):
    global map_arr
    x, y = bx, by
    while 1:
        nx = x + dxy[d][0]
        ny = y + dxy[d][1]
        if map_arr[nx][ny] == 5:
            map_arr[x][y] = 0
            return nx, ny
        if map_arr[nx][ny] == 0:
            map_arr[x][y], map_arr[nx][ny] = map_arr[nx][ny], map_arr[x][y]
            x, y = nx, ny
        else:
            break
    return x, y


n, m = map(int, input().split())
map_arr = [[validate(s) for s in input()] for _ in range(n)]
red = ()
blue = ()

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if map_arr[i][j] == 1:
            red = (i, j)
            continue
        if map_arr[i][j] == 2:
            blue = (i, j)
            continue

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
que = deque([(red, blue,0)])
result = 11
while que:
    red, blue, depth = que.popleft()
    if depth == 10:
        break
    rx, ry = red
    bx, by = blue
    for d in range(4):
        if map_arr[rx+dxy[d][0]][ry+dxy[d][1]] not in (0,5) and map_arr[bx+dxy[d][0]][by+dxy[d][1]] not in (0,5):
            continue
        map_arr[rx][ry] = 1
        map_arr[bx][by] = 2
        if (d == 0 and rx >= bx) or (d == 1 and ry >= by) or (d == 2 and rx <= bx) or (d == 3 and ry <= by):
            rnx, rny = red_move(d, rx, ry)
            bnx, bny = blue_move(d, bx, by)
        else:
            bnx, bny = blue_move(d, bx, by)
            rnx, rny = red_move(d, rx, ry)
        if map_arr[rnx][rny] == 5:
            if map_arr[bnx][bny] == 5:
                continue
            map_arr[bnx][bny] = 0
            result = min(result, depth + 1)
            break  # for 문 탈출 (while 탈출 주의)

        que.append(((rnx, rny), (bnx, bny), depth + 1))
        map_arr[rnx][rny] = 0
        map_arr[bnx][bny] = 0


print(result if result < 11 else -1)
>>>>>>> e5f09dff3cef079e85375aeef0a39d6ffa13ea44
