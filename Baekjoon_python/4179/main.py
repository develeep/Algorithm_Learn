import sys
sys.stdin = open("input.txt", "r")

###########################################################

from collections import deque

r,c = map(int,input().split())

arr = [[s for s in input()] for _ in range(r)]

def find_fire_ji(r,c):
    fire = []
    ji = ()
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'F':
                fire.append((i,j))
                continue
            if arr[i][j] == 'J':
                ji = (i,j)
    return fire, ji

dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(fire,ji):
    q = deque()
    if ji[0] == 0 or ji[0] == (r-1) or ji[1] == 0 or ji[1] == (c-1):
        return 1
    for f in fire:
        q.append((1, 'F',f))
    q.append((1, 'J',ji))
    while q:
        depth, t, (x,y) = q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0 <= nx < r and 0 <= ny < c):
                continue
            if arr[nx][ny] == '#' or arr[nx][ny] == 'F' or t == arr[nx][ny]:
                continue
            if t == 'J' and (nx == 0 or nx == (r-1) or ny == 0 or ny == (c-1)):
                return depth + 1
            arr[nx][ny] = t
            q.append((depth+1,t,(nx,ny)))
    return 'IMPOSSIBLE'

fire,ji = find_fire_ji(r,c)
print(bfs(fire,ji))