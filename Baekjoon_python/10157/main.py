import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')
##################################################

def main():
    c,r = map(int,input().split())
    k = int(input())
    arr = [[0]*c for _ in range(r)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    x,y,direction = 0,0,0
    stack = 1
    i = 1
    if k > c*r:
        return 0
    while i < k:
        arr[x][y] = i
        # print(i, c - stack)
        if direction % 2 == 0:
            if k - i -1 < r - stack:
                move = k - i
                x = x + dx[direction] * move
                y = y + dy[direction] * move
                i += move
                continue

            i += r - stack
        else:
            if i > r + r + c - 3:
                stack += 1
            if k - i <= c - stack:
                move = k - i
                x = x + dx[direction] * move
                y = y + dy[direction] * move
                i += move
                continue
            i += c - stack
        x += dx[direction] * (r - stack)
        y += dy[direction] * (c - stack)
        direction = (direction + 1)%4
    return y+1, x+1


result = main()
if result:
    print(*result)
else:
    print(0)
