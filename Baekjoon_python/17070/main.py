import sys
sys.stdin = open('input.txt', 'r')
##################################################

def find_way(x,y,position):
    cnt = 0

    if (x, y, position) in history:
        return history[(x, y, position)]

    if x == n-1 and y == n-1:
        return 1
    if position != 2 and y+1 < n and arr[x][y+1] == 0:
        cnt += find_way(x, y+1, 1)

    if position != 1 and x + 1 < n and arr[x+1][y] == 0:
        cnt += find_way(x+1, y, 2)

    if x+1 < n and y+1 < n and arr[x+1][y+1] == 0 and arr[x][y+1] == 0 and arr[x+1][y] == 0:
        cnt += find_way(x+1, y+1, 3)

    history[(x,y,position)] = cnt
    return cnt


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr[0][0] = 1
arr[0][1] = 1
history = {}
cnt = find_way(0,1,1)
print(cnt)

