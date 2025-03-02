import sys
sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque
students = [[s for s in input()] for _ in range(5)]
result = 0
dxy = [(0,1),(0,-1),(1,0),(-1,0)]
# for arr in itertools.combinations(range(25),7):
#     print(arr)
a = [(1,0),(1,1),(1,2),(1,3),(1,4),(2,4),(3,4)]
def bfs(arr):
    q = deque()
    q.append((arr[0][0],arr[0][1]))
    visited = [[0] * 5 for _ in range(5)]
    visited[arr[0][0]][arr[0][1]] = 1
    cnt = 1
    while q:
        x,y= q.popleft()
        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not(0<=nx<5 and 0<=ny<5):
                continue
            if (nx,ny) in arr and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx,ny))
    if cnt >= 7:
        return 1
    return 0
def f(idx,arr,spy):
    global result
    if len(arr) == 7:
        result += bfs(arr)
        return

    for i in range(idx,25):
        if (7- len(arr)) <= (25 - i):
            if students[i//5][i%5] == 'Y':
                if spy == 3:
                    continue
                f(i+1,arr+[(i//5,i%5)],spy+1)
            else:
                f(i+1,arr+[(i//5,i%5)],spy)

f(0,[],0)
print(result)