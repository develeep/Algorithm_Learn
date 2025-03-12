import sys
sys.stdin = open('input.txt', 'r')
##################################################
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, special, depth):
    global max_result

    flag = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if visited[nx][ny]:
            continue

        if arr[nx][ny] < arr[x][y]:
            flag = 1
            visited[nx][ny] = 1
            dfs(nx, ny, special, depth + 1)
            visited[nx][ny] = 0
            continue

        if special and arr[nx][ny] - k < arr[x][y]:
            flag = 1
            visited[nx][ny] = 1
            old = arr[nx][ny]
            arr[nx][ny] = arr[x][y] - 1
            dfs(nx, ny, 0, depth + 1)
            arr[nx][ny] = old
            visited[nx][ny] = 0

    if flag == 0:
        max_result = max(max_result, depth)
        return


T = int(input())  # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cache = {}
    max_h = 0
    for i in range(n):
        for j in range(n):
            max_h = max(max_h, arr[i][j])

    high_mountain = [(i, j) for i in range(n) for j in range(n) if arr[i][j] == max_h]
    max_result = 1
    for hx, hy in high_mountain:
        visited = [[0] * n for _ in range(n)]
        visited[hx][hy] = 1
        dfs(hx, hy, 1, 1)

    print(f'#{tc}', max_result)
