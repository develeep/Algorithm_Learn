import sys

sys.stdin = open('input.txt', 'r')


########################################
def dfs(idx):
    arr.append(idx)
    if not vector[idx]:
        return
    for i in range(v):
        if vector[idx][i] == 0:
            continue
        if i in arr:
            continue
        dfs(i)


T = 1  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    ways = list(map(int, input().split()))
    vector = [[0] * v for _ in range(v)]
    for i in range(0, len(ways), 2):
        start, end = ways[i] - 1, ways[i + 1] - 1
        vector[start][end] = 1
        vector[end][start] = 1
    arr = []
    dfs(0)
    print(f'#{tc}', '-'.join(map(lambda x: str(x + 1), arr)))
