import sys

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