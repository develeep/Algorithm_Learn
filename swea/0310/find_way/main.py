import sys

sys.stdin = open('input.txt', 'r')


########################################
def dfs(idx):
    visited[idx] = 1
    if idx == 99:
        return 1
    for i in nodes[idx]:
        if visited[i]:
            continue
        if dfs(i):
            return 1
    return 0


T = 10  # Test case 개수를 받아오는 코드

for tc in range(1, T + 1):
    t, n = map(int, input().split())
    ways = list(map(int, input().split()))
    nodes = [[] for _ in range(100)]
    for i in range(0, len(ways), 2):
        start, end = ways[i], ways[i + 1]
        nodes[start].append(end)
    visited = [0] * 100
    print(f'#{tc}', dfs(0))
