import sys

sys.stdin = open('input.txt', 'r')


###############################################################
dxy = ((0, 1), (0, -1), (-1, 0), (1, 0))


def bfs():
    global res
    cnt = len(blank) - 3
    stack = virus[:]
    visited = [[0] * m for _ in range(n)]
    while stack:
        if cnt < res:
            return 0
        x, y = stack.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] or grid[nx][ny]:
                continue

            visited[nx][ny] = 1
            cnt -= 1
            stack.append((nx, ny))

    return cnt


def dfs(idx, arr):
    global res
    if len(arr) == 3:
        for ax, ay in arr:
            grid[ax][ay] = 1
        res = max(res, bfs())
        for ax, ay in arr:
            grid[ax][ay] = 0
        return

    for i in range(idx, len(blank)):
        dfs(i + 1, arr + [blank[i]])


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
blank = []
virus = []
res = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            blank.append((i, j))
        elif grid[i][j] == 2:
            virus.append((i, j))

dfs(0, [])
print(res)
